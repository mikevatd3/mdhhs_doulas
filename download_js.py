import requests
import datetime
import pandas as pd
import json

today = datetime.datetime.now().strftime("%Y-%m-%d")

response = requests.get(
    "https://mdhhs-pres-prod.michigan.gov/DoulaMap/data/Doulas.js?version=229368"
)

file = response.content

doula_dict = json.loads(
    '{"doulas": [\n'
    + str(file.decode("utf-8"))
    .replace("};", "},")
    .replace("doulas[doulas.length] = ", "")
    .strip()
    .strip(",")
    + "\n]}"
)

df = pd.DataFrame(doula_dict["doulas"])
df.to_csv(f"raw/doulas_{today}.csv", index=False)


