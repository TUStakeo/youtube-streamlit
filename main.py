import streamlit as st
import numpy as np
import pandas as pd  
from PIL import Image
import time
st.title("streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({"1列目":[1, 2, 3, 4],
                   "2列目":[10, 20, 30, 40]})

#st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

#st.table(df)

df = pd.DataFrame(np.random.rand(20,3),columns=["a","b","c"])

st.line_chart(df)

df = pd.DataFrame(np.random.rand(100,2) / [50,50] + [35.69,139.70],
                  columns=["lat","lon"]
                  )
st.map(df)   


#if st.checkbox("show image"):
#    st.write("Display Image")
#    img = Image.open("写真.jpg") 

#    st.image(img,caption="we are best friends",use_column_width = True)

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    options=list(range(1,11))
)

"あなたの好きな数字は",option,"です"

st.write("インタラクティブなウィジェッツ")

text = st.sidebar.text_input("あなたの趣味を教えてください")
"あなたの趣味:"+text+"です。"

"おおおおおお"

condition = st.sidebar.slider("調子はどうだ?",0,100,50)
"あなたの調子は:",condition


left_column,right_column=st.beta_columns(2)
button = left_column.button("右側に文字を表示")
if button:
    right_column.write("ボタンを押しましたね!")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答")

expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答")

expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答")

st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)
"DONE!!!"


"""
# 章

## 節

### 項

```python
import streamlit as st
import numpy as np
import pandas as pd  
```


"""