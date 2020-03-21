# Лабораторна робота No6
# Регресія. Метод найменших квадратів

# sudo apt install python3-tk python3 python3-pip
# sudo pip3 install pandas seaborn matplotlib numpy statsmodels

# Завдання 2. Дослідити залежність продажів від витрат на рекламу на
# телебаченні, радіо та в газеті.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Advertising.csv");
# print(data.head()); print();
# print(data.shape); print();

# sns.pairplot(data);
# plt.show();

# fig, axs = plt.subplots(1, 3, sharey=True)
# plt.show(data.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 8)));
# plt.show(data.plot(kind='scatter', x='radio', y='sales', color='red', ax=axs[1]));
# plt.show(data.plot(kind='scatter', x='newspaper', y='sales', color='green', ax=axs[2]));
# print();

# print(data.corr());	# кореляція даних Пірсона - показує існування
#			# лінійної залежності між величинами
# print();

import statsmodels.formula.api as smf
#
lm = smf.ols(formula='sales~TV', data=data).fit();
# # print the coefficients
# print(lm.params); print();

# потрібно створити DataFrame, оскільки його очікує інтерфейс формули Statsmodels
X_new = pd.DataFrame({'TV': [50]});
print(X_new.head());
# використати модель, щоб зробити прогнози на нове значення
print(lm.predict(X_new)); print();
