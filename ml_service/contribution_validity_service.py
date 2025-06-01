from ml_service.get_data import read_data
from ml_service.find_max_contribution_from_company import check_company_contribution
from ml_service.find_the_expected_size import predict_the_contribution
import math
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def contribution(expected_item,expected_contribution):

    try:
        df_historical = read_data(item_id=expected_item)
        predicted_total, historical_max = check_company_contribution(df=df_historical)
        max_size = predict_the_contribution(df=df_historical,total_expected=expected_contribution)
        max_size['scaled_prediction'] = max_size['scaled_prediction'].apply(math.ceil)

        if expected_contribution <= predicted_total:
            return max_size.to_json(orient='records'), 200

        elif expected_contribution <= historical_max:
            return max_size.to_json(orient='records'), 200

        else:
            logging.error("Our suppliers won't be able to do this request")
            return {"resMsg": "Our suppliers won't be able to do this request"}, 400

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return {"resMsg": "Error occured while processing the request"}, 501