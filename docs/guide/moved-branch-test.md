# Pet listing guide

This page explains how to list pets in the Petstore API.

## List pets

Call `GET /pets` to list pets.
The API lists pets in the order they were added.

## Filter pets

Pass the `status` query parameter to filter pets by status.
The `status` parameter accepts `available`, `pending` and `sold`.

## Limits

The API returns at most 50 pets per request.
