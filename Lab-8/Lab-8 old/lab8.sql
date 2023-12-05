CREATE DATABASE TimeSeriesAnalysisDB;
CREATE TABLE stocks (
    symbol VARCHAR(10),
    date DATE,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume INT,
    PRIMARY KEY (symbol, date)
);

CREATE TABLE technical_indicators (
    symbol VARCHAR(10),
    date DATE,
    sma_20 FLOAT,
    rsi FLOAT,
    macd FLOAT,
    PRIMARY KEY (symbol, date),
    FOREIGN KEY (symbol, date) REFERENCES stocks(symbol, date)
);

CREATE TABLE news_sentiment_analysis (
    date DATE,
    positive_articles INT,
    negative_articles INT,
    neutral_articles INT,
    PRIMARY KEY (date)
);

CREATE TABLE external_events (
    date DATE,
    event_description VARCHAR(255),
    PRIMARY KEY (date),
    FOREIGN KEY (date) REFERENCES news_sentiment_analysis(date)
);
