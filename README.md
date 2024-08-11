![image](https://github.com/user-attachments/assets/9d7a5355-11ec-4063-b9d9-38be1ed8d4bd)

![Uploading image.png…]()


ENG

How do I launch a project?


To test the bot in demo mode, run start.bat
To use the bot, change the configuration in the .env file (it was created only for the OKKHB exchange, by analogy, take the API keys of the Binance, Bybit, etc. exchanges and create a cluster in .env, take cluster examples from the same file
The neural network project for cryptotrading is aimed at developing and implementing a system using machine learning methods to analyze the cryptocurrency market and make trading decisions. This system provides users with automatic recommendations for buying and selling cryptocurrencies based on complex algorithms and analysis of large amounts of data.
The project supports the API of all popular exchanges
OKX, Bybit, Binance, etc.
The developers of this project are leading crypto investors together with a team of programmers.
Also a unique feature: support for crypto wallets (including extensions)
- Exodus
- Electrum
- Atomic
- Trust
- Metamask
- Phantom
and many others


#### Project objectives

- Automation of trading operations: Creation of a system capable of independently making decisions on the purchase and sale of cryptocurrencies.
- Increase profits: Optimize trading strategies to maximize profits through the use of predictive models.
- Risk reduction: The application of risk management methods to minimize possible losses.

#### Technical aspects
1. Data collection
 - Historical data on cryptocurrencies (prices, trading volumes, capitalization).
 - Market indicators and signals (RSI, MACD, SMA).
 - News and social media (Twitter, Reddit, news sites).

2. Data preprocessing
 - Clearing data from noise and anomalies.
 - Normalization and standardization of data.
 - Creation of time series and selection of significant features.

3. Neural network architecture
 - Neural network type: LSTM (Long Short-Term Memory) for time series analysis.
 - Neural network layers: An input layer, several hidden LSTM layers, a fully connected output layer.
 - - Hyperparameters: Layer sizes, learning rate, number of epochs, etc.

4. Model Training
 - Data separation into training, validation and test samples.
 - Using optimization methods (Adam, RMSProp).
 - Regularization to prevent overfitting (dropout, L2-regularization).

5. Evaluation of the model
 - Evaluation metrics: MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), R^2.
 - Cross-validation to check the stability of the model.
 - Backtesting: testing the model on historical data to assess its effectiveness.

6. Integration and deployment
 - Development of an API for interacting with cryptocurrency exchanges.
 - Creating a simple user interface for data visualization and system management.
 - Deployment of the model on cloud platforms (AWS, Google Cloud).

RU

 - Как запустить проект?
Для проверки бота в демо режиме, запустите start.bat
Для использования бота - измените конфигурацию в .env файле (она создана только для биржы OKXБ по аналогии возьмите API-keys бирж Binance, Bybit и т.д. и создайте кластер в .env, примеры кластера возьмите из этого же файла
Проект нейросети для криптотрейдинга направлен на разработку и внедрение системы, использующей методы машинного обучения для анализа криптовалютного рынка и принятия торговых решений. Эта система предоставляет пользователям автоматические рекомендации по покупке и продаже криптовалют, основываясь на сложных алгоритмах и анализе больших объемов данных.
Проект поддерживает API всех популярных бирж
OKX, Bybit, Binance и др.
Разработчики данного проекта - ведущие криптоинвесторы совместно с командой программистов.
Также уникальная функция: поддержка криптокошельков (расширений в т.ч.)
- Exodus
- Electrum
- Atomic
- Trust
- Metamask
- Phantom
и множество других


#### Цели проекта
- Автоматизация торговых операций: Создание системы, способной самостоятельно принимать решения о покупке и продаже криптовалют.
- Увеличение прибыли: Оптимизация стратегий торговли для максимизации прибыли за счет использования прогнозирующих моделей.
- Снижение рисков: Применение методов управления рисками для минимизации возможных убытков.

#### Технические аспекты
1. Сбор данных
   - Исторические данные по криптовалютам (цены, объемы торгов, капитализация).
   - Рыночные индикаторы и сигналы (RSI, MACD, SMA).
   - Новости и социальные медиа (Twitter, Reddit, новостные сайты).

2. Предобработка данных
   - Очистка данных от шумов и аномалий.
   - Нормализация и стандартизация данных.
   - Создание временных рядов и выборка значимых признаков.

3. Архитектура нейросети
   - Тип нейросети: LSTM (Long Short-Term Memory) для анализа временных рядов.
   - Слои нейросети: Входной слой, несколько скрытых слоев LSTM, полносвязный выходной слой.
   - Гиперпараметры: Размеры слоев, скорость обучения, количество эпох и т.д.

4. Обучение модели
   - Разделение данных на обучающую, валидационную и тестовую выборки.
   - Использование методов оптимизации (Adam, RMSprop).
   - Регуляризация для предотвращения переобучения (dropout, L2-регуляризация).

5. Оценка модели
   - Метрики оценки: MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), R^2.
   - Кросс-валидация для проверки устойчивости модели.
   - Бэктестинг: тестирование модели на исторических данных для оценки ее эффективности.

6. Интеграция и развертывание
   - Разработка API для взаимодействия с биржами криптовалют.
   - Создание простого пользовательского интерфейса для визуализации данных и управления системой.
   - Развертывание модели на облачных платформах (AWS, Google Cloud).
 
