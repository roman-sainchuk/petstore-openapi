# Order guide

This page explains how to place and track orders in the Petstore API.

## Place an order

Call `POST /store/order` to place an order.
An order holds one pet.

## Track an order

Call `GET /store/order/{orderId}` to read an order.
The `status` field shows `placed`, `approved` or `delivered`.

## Limits

The store keeps an order for 30 days.
