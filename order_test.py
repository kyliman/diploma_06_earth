# Анастасия Куликова, 06-earth — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data
import json


# Тест 1. Успешное создание заказа
def test_create_order_get_success_response():
    create_order_response = sender_stand_request.post_new_order(data.order_body)

    # Проверяется, что код ответа на запрос создания заказа равен 201
    assert create_order_response.status_code == 201

    # Проверяется, что в ответе есть поле track и оно не пустое
    assert create_order_response.json()["track"] != ""

    track = create_order_response.json()["track"]

    # Получение заказа по его номеру (track)
    get_order_response = sender_stand_request.get_order_by_track(track)

    # Проверяется, что код ответа равен 200
    assert get_order_response.status_code == 200
