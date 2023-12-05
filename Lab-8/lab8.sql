CREATE DATABASE timeseriesdb;
use timeseriesdb;
-- Creating Table 'stocks'
CREATE TABLE stocks (
    symbol VARCHAR(10),
    date DATE,
    open FLOAT,
    close FLOAT,
    high FLOAT,
    low FLOAT,
    volume INT,
    PRIMARY KEY (symbol, date)  -- Assuming symbol and date together form a unique key
);

-- Creating Table 'technical_indicators'
CREATE TABLE technical_indicators (
    symbol VARCHAR(10),
    date DATE,
    sma_20 FLOAT,
    rsi FLOAT,
    macd FLOAT,
	PRIMARY KEY (symbol, date), -- Assuming symbol and date together form a unique key
	 FOREIGN KEY (symbol, date) REFERENCES stocks(symbol, date)
);

-- Creating Table 'news_sentiment_analysis'
CREATE TABLE news_sentiment_analysis (
    date DATE PRIMARY KEY,
    positive_articles INT,
    negative_articles INT,
    neutral_articles INT
);

-- Creating Table 'external_events' with Foreign Key referencing 'news_sentiment_analysis' table
CREATE TABLE external_events (
    date DATE,
    event_description VARCHAR(300),
    PRIMARY KEY (date, event_description),
	FOREIGN KEY (date) REFERENCES news_sentiment_analysis(date)
);


