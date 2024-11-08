def rsi(df, column = 'price', window = 14):
    df_copy = df[[column]].copy()
    
    # Calculate daily price changes
    df_copy['change'] = df_copy[column].diff()

    # Calculate gains and losses
    df_copy['gain'] = df_copy['change'].where(df_copy['change'] > 0, 0)
    df_copy['loss'] = -df_copy['change'].where(df_copy['change'] < 0, 0)

    # Calculate the average gain and loss
    df_copy['avg_gain'] = df_copy['gain'].rolling(window=window, min_periods=1).mean()
    df_copy['avg_loss'] = df_copy['loss'].rolling(window=window, min_periods=1).mean()

    # Calculate the Relative Strength (RS)
    df_copy['rs'] = df_copy['avg_gain'] / df_copy['avg_loss']

    # Calculate RSI
    df_copy['rsi'] = 100 - (100 / (1 + df_copy['rs']))
    
    return df_copy['rsi']

def bbands(df, price_column='price', window=20, std_dev_multiplier=2):
    df_copy= df[[price_column]].copy()
    df_copy['SMA'] = df_copy[price_column].rolling(window=window).mean()
    df_copy['STD'] = df_copy[price_column].rolling(window=window).std()

    # Calculate Upper and Lower Bollinger Bands
    df_copy['Upper Band'] = df_copy['SMA'] + (df_copy['STD'] * std_dev_multiplier)
    df_copy['Lower Band'] = df_copy['SMA'] - (df_copy['STD'] * std_dev_multiplier)

    return df_copy['Lower Band'], df_copy['Upper Band']