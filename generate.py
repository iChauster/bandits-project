import pandas as pd

with open("./yelp_dataset/yelp_academic_dataset_review.json", "r") as f:
	df = pd.read_json(f)
	df.