class Products:
    def __init__(self):
        self.products = [
            {
                "id": "0001",
                "description": "AULA DE FLASK FULL ATUALIZADO",
                "amount": 1.00,
                "quantity": 1,
                "weight": 200,
                "price": 1.0
            },
            {
                "id": "0002",
                "description": "Fiat Uno com escadinha",
                "amount": 50,
                "quantity": 1,
                "weight": 1000,
                "price": 1
            },
        ]

    def get_all(self):
        return self.products

    def get_one(self, item_id):
        p = [p for p in self.products if p['id'] == item_id]
        if len(p) > 0:
            return p[0]
        else:
            return False
