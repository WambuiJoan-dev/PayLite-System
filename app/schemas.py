
from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))


class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=100)
    )
    national_id = fields.Str(
        required=True,
        validate=validate.Length(equal=8)  
    )
    credit_status = fields.Str(
        required=False,
        validate=validate.OneOf(["Active", "Completed", "Defaulted"])
    )


class PhoneSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50)
    )
    model = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=50)
    )
    price = fields.Int(
        required=True,
        validate=validate.Range(min=1)  
    )
    stock_quantity = fields.Int(
        required=True,
        validate=validate.Range(min=0)
    )


class SaleSchema(Schema):
    id = fields.Int(dump_only=True)
    total_price = fields.Int(dump_only=True)  
    deposit_paid = fields.Int(
        required=True,
        validate=validate.Range(min=0)
    )
    balance_due = fields.Int(dump_only=True)
    installment_amount = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )
    status = fields.Str(
        dump_only=True 
    )
    customer_id = fields.Int(required=True)
    phone_id = fields.Int(required=True)


class PaymentSchema(Schema):
    id = fields.Int(dump_only=True)
    amount_paid = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )
    date_paid = fields.DateTime(dump_only=True)
    next_due_date = fields.DateTime(dump_only=True)
    sale_id = fields.Int(required=True)
