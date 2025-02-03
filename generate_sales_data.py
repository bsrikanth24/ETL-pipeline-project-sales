from faker import Faker
import pandas as pd
import random

# Inicializar Faker
fake = Faker()

# Configurações
num_records = 100  # Número de registros a gerar

# Gerar dados fictícios
data = []
for _ in range(num_records):
    record = {
        "sale_id": fake.uuid4(),
        "customer_name": fake.name(),
        "customer_email": fake.email(),
        "product": fake.word(),
        "quantity": random.randint(1, 10),
        "price_per_unit": round(random.uniform(5.0, 100.0), 2),
        "sale_date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
    }
    data.append(record)

# Converter para DataFrame
df = pd.DataFrame(data)

# Salvar em CSV
df.to_csv("sales_data.csv", index=False)
print("Dados gerados com sucesso: sales_data.csv")
