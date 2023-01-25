import pickle
import pandas as pd
import re
from pathlib import Path



BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/tfidf.pkl", "rb") as f:
        tfidf = pickle.load(f)





def predict_pipeline(text,model_pkl):
    # text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    # text = re.sub(r"[[]]", " ", text)
    # text = text.lower()
    with open(f"{BASE_DIR}/{model_pkl}.pkl", "rb") as f:
        model = pickle.load(f)
    texts = pd.Series(text)
    print(texts)
    tfidf_text = tfidf.transform(texts).toarray()
    print(tfidf_text.shape)
    pred = model.predict(tfidf_text)
    print(pred)
    return pred[0]