# Pet listing and filtering guide

This page explains how to list and filter pets in the Petstore API.

## List pets

Call `GET /pets` to fetch the list of pets.
The API lists pets by the date they were added.

## Filter pets

Use the `status` query parameter to filter pets by status.
The `status` parameter accepts `available`, `pending`, or `sold`.

## Limits

The API returns up to 25 pets per request.
