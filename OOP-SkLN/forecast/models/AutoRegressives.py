from AutoRegressiveModels import *

class AutoRegressives():

    def __init__(self, dt:'pd.DataFrame', target_variable:str, *args):
      '''
	         Initialization Parameters. It assummes your target values are in a columnar form. 
	        :param dt: Data with all the observations
	        :param target_variable: variable that you would like to forecast
    	'''   
      self.dt = dt 
      self.target = dt[target_variable]
      self.dependent = dt.drop(columns=[target_variable])

    def AR_model(self, model:str='arima', n_forecast):
    	'''
	        First test for seasonality and trend in data with an Augmented Dicker Fuller Test and KPSS test. Then, based on the 
          choosen model ('arima' for Seasonal Arima, 'sem' for Simple Exponential Smoothing, 'holt' for Holt,
          'holt-winters' for Holt-Winters) implements an AutoRegressive model for Forecasting.
          
          Input:
	        :param model: which of the four ML models to implement according to the documentation
	        :param n_forecast: number of desired forecasted values 
          
          Output:
          forecast: Forecast for the next n_forecast observations
          aic: AIC of model
          bic: BIC of model
          mse: MSE of model
          sse: SSE of model
          model: model choosen for forecasting
    	'''
      
      # Test Seasonality and Trend in Data
      model, regularization = preprocess_AR().test(self.target)
      
      # Fit model for forecast
      if model == 'arima':
         forecast, aic, bic, mse, sse = arima(obs=self.target, 
                                              p_mean = regularization, 
                                              boxcox = regularization,  
                                              n_forecast = n_forecast)
      elif model == 'sem':
         forecast, aic, bic, mse, sse  = sem(obs=self.target,
                                             p_mean = regularization, 
                                             boxcox = regularization,  
                                             n_forecast = n_forecast)
      elif model == 'holt':
         forecast, aic, bic, mse, sse = holt(obs=self.target,
                                             p_mean = regularization, 
                                             boxcox = regularization,  
                                             n_forecast = n_forecast)
      elif model == 'holt-winters':
         forecast, aic, bic, mse, sse = holt_winters(obs=self.target,
                                             p_mean = regularization, 
                                             boxcox = regularization,  
                                             n_forecast = n_forecast)
       
      return (forecast, aic, bic, mse, sse, model)
 