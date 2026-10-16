# Clean Data

The clean data files are stored on Google Drive because they exceed GitHub file limit

- [clean.csv](https://drive.google.com/file/d/1wiglgftAE55E4dyefZlHEfWmEc4UXQph/view?usp=sharing)
- [clean.parquet](https://drive.google.com/file/d/1VV0JLvtGmc88sN0zx8AxctvA4C-VClCs/view?usp=sharing)

## How to Load
Use this as the first cell in every new notebook:

```python
import gdown, pandas as pd
gdown.download(id='1VV0JLvtGmc88sN0zx8AxctvA4C-VClCs', output='clean.parquet', quiet=False)
df = pd.read_parquet('clean.parquet')
```
