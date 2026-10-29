# Order guide

This page explains how to place and track orders in the Petstore API.

## Place an order

Send a `POST /store/order` request to place an order.
An order holds one pet.

## Track an order

Send a `GET /store/order/{orderId}` request to read an order.
The `status` field shows `placed`, `approved` or `delivered`.

## Limits

The store keeps an order for 60 days.
