import configuration
import requests
import data

def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
        headers=data.headers
    )

def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + str(track),
        headers=data.headers
    )
