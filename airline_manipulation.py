import os
# from sklearn import preprocessing
#import pandas as pd
# from datamanipulation.logs.data_preprocessing import make_col_positive
import numpy as np

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)
# data = pd.read_csv("espresso_python_hacking/data/flights.csv")
#data = pd.read_csv("../../data/flights.csv")
#data.shape()
#print(data.head())
import sys

# TODO: Initialise a simple logger and set the desired format to be: TIME LEVEL-module-function-line number-message

import logging
logging.basicConfig(level='DEBUG')
log = logging.getLogger("my-logger")
log.info( "Hello, world")


# import logging
# logger = logging.getLogger('root')
# FORMAT = "[%(asctime)s:%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
# logging.basicConfig(format=FORMAT)
# logger.setLevel(logging.DEBUG)
# logger.debug('Stuff')

def transform_data(data):
    """
    Function to transform data according to some pre-defined steps.

    :param data: data to transform, dataframe format
    :return: transformed data
    """

    # TODO: drop column 'DAY_OF_WEEK'
    data = data.drop('DAY_OF_WEEK', axis=1)

    # TODO: Rename column 'WHEELS_OFF' to 'HAS_WHEELS'

    data = data.rename(columns={'WHEELS_OFF': 'HAS_WHEELS'})

    # TODO: Fill blanks in column 'AIR_SYSTEM_DELAY' with the average of the values
    data['AIR_SYSTEM_DELAY'] = data['AIR_SYSTEM_DELAY'].fillna((data['AIR_SYSTEM_DELAY'].mean()))

    # TODO: Scale values between 0 and 1 in 'DEPARTURE_DELAY' and put them in 'DEPARTURE_DELAY_NORMALISED'
    data['DEPARTURE_DELAY_NORMALISED'] = (data['DEPARTURE_DELAY'] - data['DEPARTURE_DELAY'].min()) / (data['DEPARTURE_DELAY'].max() - data['DEPARTURE_DELAY'].min())

    # TODO: Make 'ARRIVAL_DELAY' column positive using a function imported from data_preprocessing.py
    from data_preprocessing import make_col_positive
    make_col_positive(data, 21)

    # TODO: take the log of the column DEPARTURE_DELAY

#    make_col_positive(data, 21)
    from data_preprocessing import log_transform
    log_transform(data,10)

    return data


if __name__ == "__main__":
    '''
    HOMEWORK: Write a function that outputs insights into the data. I.e. aggregated data, plots etc. that will
    tell a compelling story to Heathrow about trends that we have discovered in the airline industry.
    
    The output should be the repository that helped produce the insight and a deck (.pdf, no longer that 5 slides)
    which would be used to present the insights to the client. 
    
    Please do not spend more than 3 hours on this.
    '''
    print(sys.path)
#    flights_data = None # TODO: Import flight data
    flights_data = pd.read_csv("../../data/flights.csv")
    transformed = transform_data(flights_data)
    print(transformed.head())
    print(transformed.shape)

#WORKed for plotting
#--------------
    import matplotlib.pyplot as plt
    #plt.show(transformed['DEPARTURE_DELAY'].hist())
#--------------

#https://www.kaggle.com/typewind/draw-a-radar-chart-with-python-in-a-simple-way
    from math import pi
    import seaborn as sns

    # labels=np.array(['AIR_SYSTEM_DELAY', 'SECURITY_DELAY, ''AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY'])
    # stats=transformed.loc[:,labels].mean()
    #
    # angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    # # close the plot
    # stats=np.concatenate((stats,[stats[0]]))
    # angles=np.concatenate((angles,[angles[0]]))
    #
    #
    # fig=plt.figure()
    # ax = fig.add_subplot(111, polar=True)
    # ax.plot(angles, stats, 'o-', linewidth=2)
    # ax.fill(angles, stats, alpha=0.25)
    # ax.set_thetagrids(angles * 180/np.pi, labels)
    # ax.set_title('Radar plot of airline v delay type')
    # ax.grid(True)
    #
    # plt.show()


    # fig, axs = plt.subplots(2, 2, figsize=(5, 5))
    # axs[0, 0].hist(transformed[0])
    # axs[1, 0].scatter(transformed[0], transformed[1])
    # axs[0, 1].plot(transformed[0], transformed[1])
    # axs[1, 1].hist2d(transformed[0], transformed[1])
    #
    # plt.show()



    #fig = plt.figure(transformed['DEPARTURE_DELAY'].hist())
    #fig = plt.figure()
    #fig.savefig('graph.png')
    #from ../../src/plotting/data_visualisations import flights_visuals
    #flights_visuals(transformed, 21)


#    fig.savefig('graph.png')

    #import seaborn as sns
#-------------------------
    # plt.hist(transformed['DEPARTURE_DELAY'], alpha=.3)
    # plt.show()
#-------------------------
    #plt.hist(transformed.mean(), alpha=.3)
    #sns.rugplot(transformed['DEPARTURE_DELAY'])
    #sns.rugplot(transformed['DEPARTURE_DELAY'])
    #sns.set_axis_labels("Day", "Total Bill");
    #plt.show()

#Works for creating a file. but not sure how to populate it with a graph
#---------------------
#    plt.savefig('graph.pdf')
#---------------------

#Works for creating a pivot table
#----------------
#   table = pd.pivot_table(transformed, values='DEPARTURE_DELAY', index=['AIRLINE'], aggfunc=np.sum)
#   print(table)
#----------------

    #---------Pivot by Airline
    Airline_Pivot_table = pd.pivot_table(transformed, values=['DEPARTURE_DELAY','AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY'], index=['AIRLINE'], aggfunc=np.mean)
#    df = df.reindex(df_pivot['Value'].sort_values(by=2012, ascending=False).index)
    #transformed = transformed.reindex(table['DEPARTURE_DELAY'].sort_values('DEPARTURE_DELAY', ascending=False).index)
#    table.sort_values(by='DEPARTURE_DELAY', ascending=False)
    Airline_Pivot_table.plot()
    plt.show()
    plt.savefig('Airline_Pivot.pdf')
    print(Airline_Pivot_table)

    #------- Pivot by Tail Number
    Tail_Delay_Pivot_table = pd.pivot_table(transformed, values=['DEPARTURE_DELAY','AIRLINE_DELAY'], index=['TAIL_NUMBER'], aggfunc=np.mean)
#    df = df.reindex(df_pivot['Value'].sort_values(by=2012, ascending=False).index)
    #transformed = transformed.reindex(table['DEPARTURE_DELAY'].sort_values('DEPARTURE_DELAY', ascending=False).index)
#    table.sort_values(by='DEPARTURE_DELAY', ascending=False)
    Tail_Delay_Pivot_table.plot()
    Tail_Delay_Pivot_table = Tail_Delay_Pivot_table.sort_values('AIRLINE_DELAY', ascending=False)
    plt.show()
    plt.savefig('Tail_Delay_Pivot.pdf')
    print(Tail_Delay_Pivot_table)
    #print(Tail_Number_Pivot_table.sort_values('AIRLINE_DELAY', ascending=False))


    Tail_Cancellation_Pivot_table = pd.pivot_table(transformed, values=['CANCELLED', 'AIRLINE_DELAY'], index=['TAIL_NUMBER'], aggfunc=np.sum)
    Tail_Cancellation_Pivot_table = Tail_Cancellation_Pivot_table.sort_values('AIRLINE_DELAY', ascending=False)
    print(Tail_Cancellation_Pivot_table)
    plt.savefig('Tail_Cancellation.pdf')


#    print(transformed.head())
    #sns.lmplot('y',data=transformed['DEPARTURE_DELAY'])

    # from fpdf import FPDF
    #
    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=12)
    # pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
    # pdf.cell(200, 10, Airline_Pivot_table)
    # pdf.output("simple_demo.pdf")


    #path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    #config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
#works for outputting to pdf via html
#-----------------
    import pdfkit
    Airline_Pivot_table.to_html('test.html')
    PdfFilename='pdfPrintOut.pdf'
    pdfkit.from_file('test.html', PdfFilename)
#---------------------

    # f = open('test.html','w')
    #
    # message = Tail_Delay_Pivot_table.to_html
    #
    # f.write(message)
    # f.close()
    #
    # PdfFilename='pdfPrintOut.pdf'
    # pdfkit.from_file('test.html', PdfFilename)

    # df_html_output = Airline_Pivot_table.to_html)
    # html.append(df_html_output)
    #
    # df_html_output = Tail_Delay_Pivot_table.to_html(na_rep = "", index = False).replace('<th>','<th style = "background-color: red">')
    # test.append(df_html_output)
    # body = '\r\n\n<br>'.join('%s'%item for item in html)
    # msg.attach(MIMEText(body, 'html'))
