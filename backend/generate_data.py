import random
import pandas as pd

data = []

for _ in range(5000):
    build_time = random.randint(50, 400)
    test_failures = random.randint(0, 10)
    code_changes = random.randint(1, 100)
    past_failures = random.randint(0, 5)
    deploy_time = random.randint(100, 900)

    risk_score = (
        0.3 * (test_failures / 10) +
        0.2 * (past_failures / 5) +
        0.2 * (build_time / 400) +
        0.2 * (deploy_time / 900) +
        0.1 * (code_changes / 100)
    )

    label = 1 if risk_score > 0.5 else 0

    data.append([
        build_time,
        test_failures,
        code_changes,
        past_failures,
        deploy_time,
        label
    ])

df = pd.DataFrame(data, columns=[
    "build_time",
    "test_failures",
    "code_changes",
    "past_failures",
    "deploy_time",
    "label"
])

df.to_csv("../data/dataset.csv", index=False)

print("Dataset created!")