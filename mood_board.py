import streamlit as st
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import requests
import pytz

def app():

    st.markdown("<p style='text-align: left;font-size: 45px;font-weight: bold;'>HOW ARE YOU DOING, TODAY?</p>"
                , unsafe_allow_html=True)

    st.markdown("<p style='text-align: right;font-size: 24px;font-weight: bold; color: #f46524;'> - MOOD BOARD - </p>"
                , unsafe_allow_html=True)
    st.write('----')


    def generate_data():
        options = {"7 days": 7, "14 days": 14,"30 days": 30, "90 days": 90}

        # Create the dropdown menu
        selected_option = st.selectbox("Select the number of days:", list(options.keys()))

        # Retrieve the numerical value of the selected option
        selected_days = options[selected_option]


        url = 'https://hayd1621-docker-v2-lempkfijgq-ew.a.run.app/fetch_mood_board'
        # url = 'http://127.0.0.1:8000/fetch_mood_board'
        response = requests.get(url).json()['response']
        end = dt.datetime.strptime(max(response.keys()), "%Y-%m-%d").date()
        dates = list(reversed([end - dt.timedelta(days=i) for i in range(selected_days)]))


        data = [-1]*selected_days

        for date in dates:
            idx = dates.index(date)
            date_dt = date.strftime('%Y-%m-%d')
            if date_dt in response.keys():
                data[idx] = response[date_dt]
        return dates, data

    def calendar_array(dates, data):
        i, j = zip(*[d.isocalendar()[1:] for d in dates])
        i = np.array(i) - min(i)
        j = np.array(j) - 1
        ni = max(i) + 1

        calendar = np.nan * np.zeros((ni, 7))
        calendar[i, j] = data
        return i, j, calendar

    def calendar_heatmap(ax, dates, data):
        i, j, calendar = calendar_array(dates, data)
        # im = ax.imshow(calendar, interpolation='none', cmap='summer')
        # label_days(ax, dates, i, j, calendar)
        # label_months(ax, dates, i, j, calendar)
        # ax.figure.colorbar(im)

        mood_colors = {
            -1: (1, 1, 1, 0),  # white with alpha 0 for transparency (no color)
            0: '#84c9ff',          # angry
            1: '#0168c9',        # disgusted
            2: '#ffacab',       # fearful
            3: '#2ab09d',       # happy
            4: '#7eefa1',         # neutral
            5: '#ff2a2b',         # sad
            6: '#ffd16a'        # surprised
        }

        # Create a list of colors for the colormap
        cmap = mcolors.ListedColormap([mood_colors[x] for x in range(-1, 7)])

        # Normalize the color map to the data range
        norm = mcolors.BoundaryNorm(np.arange(-1.5, 7.5, 1), cmap.N)

        # Create the heatmap
        im = ax.imshow(calendar, interpolation='none', cmap=cmap, norm=norm)

        label_days(ax, dates, i, j, calendar)
        label_months(ax, dates, i, j, calendar)
        cbar = ax.figure.colorbar(im, ticks=np.arange(-1, 7), fraction=0.02, pad=0.04)
        cbar.ax.set_yticklabels(['No Value', 'Angry', 'Disgusted', 'Fearful', 'Happy', 'Neutral', 'Sad', 'Surprised'])

        # Adjust the layout
        ax.figure.tight_layout()

    def label_days(ax, dates, i, j, calendar):
        ni, nj = calendar.shape
        day_of_month = np.nan * np.zeros((ni, 7))
        day_of_month[i, j] = [d.day for d in dates]

        for (i, j), day in np.ndenumerate(day_of_month):
            if np.isfinite(day):
                ax.text(j, i, int(day), ha='center', va='center')

        ax.set(xticks=np.arange(7),
            xticklabels=['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])
        ax.xaxis.tick_top()

    def label_months(ax, dates, i, j, calendar):
        month_labels = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                                'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        months = np.array([d.month for d in dates])
        uniq_months = sorted(set(months))
        yticks = [i[months == m].mean() for m in uniq_months]
        labels = [month_labels[m - 1] for m in uniq_months]
        ax.set(yticks=yticks)
        ax.set_yticklabels(labels, rotation=90)

    # Show the figure in Streamlit

    dates, data = generate_data()
    fig, ax = plt.subplots(figsize=(6, 6))
    calendar_heatmap(ax, dates, data)
    # plt.show()
    st.pyplot (fig)
