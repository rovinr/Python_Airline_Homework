import numpy as np


def identify_quant_cols(
        # TODO: add any arguments here
):
    # TODO: write code that will return a list of the quantitative columns in a dataframe
    pass


def make_col_positive(
        #identify the smallest negative number, and add that to the entire dataset to shift everything into positive
        # TODO: add any arguments here
        parameter_data, column_number
):
    # TODO: Add transformations here to make an entire dataframe column positive.
    #parameterdata['ARRIVAL_DELAY'] = data['ARRIVAL_DELAY'].abs()
    absolute_min = abs(parameter_data[parameter_data.columns[column_number]].min())
#    parameter_data['ARRIVAL_DELAY'] = parameter_data['ARRIVAL_DELAY'] + absolute_min
    parameter_data[parameter_data.columns[column_number]] = parameter_data[parameter_data.columns[column_number]] + absolute_min + 1

    pass


def log_transform(
        # log is only useful on a positive data set. so depends on the make col positive function above
        # TODO: add any arguments here
        parameter_data, column_number
):
    # TODO: Add any code here to log transform an entire column.

    #parameter_data[parameter_data.columns[column_number]] = make_col_positive(parameter_data, 21)
    make_col_positive(parameter_data, column_number)

#https://stackoverflow.com/questions/37890849/pandas-series-log-normalize

    import numpy as np

    parameter_data[parameter_data.columns[column_number]] = np.log(parameter_data[parameter_data.columns[column_number]])
    pass


