from ml_service.get_data import read_data
from ml_service.find_max_contribution_from_company import check_company_contribution
from ml_service.find_the_expected_size import predict_the_contribution
import math


def contribution(expected_item,expected_contribution):

    try:
        df_historical = read_data(item_id=expected_item)
        predicted_total, historical_max = check_company_contribution(df=df_historical)
        max_size = predict_the_contribution(df=df_historical, item_id=expected_item,total_expected=expected_contribution)
        max_size['scaled_prediction'] = max_size['scaled_prediction'].apply(math.ceil)

        if expected_contribution <= predicted_total:
            return max_size.to_json(orient='records'), 200

        elif expected_contribution <= historical_max:
            return max_size.to_json(orient='records'), 200

        else:
            return {"text": "Our company won't be able to do this request"}, 400

    except Exception as e:
        return {"error": str(e)}, 500