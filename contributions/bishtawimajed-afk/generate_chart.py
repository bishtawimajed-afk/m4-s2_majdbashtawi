import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup Styling
sns.set_theme(style="whitegrid")
sns.set_palette("colorblind")

# 2. Load/Create Data 
# ملاحظة: في النسخة النهائية يفضل وضع ملف CSV صغير أو استخدام الكود أدناه لتوليد بيانات مشابهة لبياناتك
def get_data():
    # هذه محاكاة للبيانات التي ظهرت في صورتك (Electronics, Clothing, etc.)
    # في مشروعك الحقيقي، يمكنك استخدام: df = pd.read_csv('sample_data.csv')
    import numpy as np
    categories = ['Electronics', 'Clothing', 'Beverage', 'Books', 'Sports', 'Garden']
    data = []
    for cat in categories:
        # توليد قيم عشوائية تحاكي الـ Boxplot في الصورة
        base = np.random.normal(50, 20, 50) 
        data.extend([(cat, val) for val in base if val > 0])
    return pd.DataFrame(data, columns=['category', 'revenue'])

df = get_data()

# 3. Create Refined Plot
fig, ax = plt.subplots(figsize=(10, 6))

sns.boxplot(
    data=df, 
    x="category", 
    y="revenue", 
    hue="category", 
    palette="colorblind",
    showfliers=True, # لإظهار النقاط البعيدة Outliers
    ax=ax
)

# 4. Refinement (Publication Quality)
ax.set_title("Electronics and Books Drive Higher Variance in Transaction Values", 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel("Product Category", fontsize=12)
ax.set_ylabel("Revenue per Order (JOD)", fontsize=12)
plt.xticks(rotation=0) # جعل الكلمات أفقية لسهولة القراءة

# إزالة الزوائد (Chart Junk)
sns.despine(left=True, bottom=True)

# 5. Save Output
plt.savefig('chart.png', dpi=150, bbox_inches='tight')
print("Chart generated successfully as chart.png")