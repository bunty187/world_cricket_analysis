import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from streamlit import components
from plotly.subplots import make_subplots


def fetch_batting_data(df):
    data = df
    highest_total_runs = data.groupby(['Innings Player', 'Country']).agg(
        {'Innings Runs Scored Num': 'sum', 'Innings Runs Scored': 'max', '50s': 'sum', '100s': 'sum'})
    highest_total_runs['Innings Runs Scored Num'] = highest_total_runs['Innings Runs Scored Num'].fillna(0)
    highest_total_runs['Innings Runs Scored'] = highest_total_runs['Innings Runs Scored'].fillna(0)
    highest_total_runs['50s'] = highest_total_runs['50s'].fillna(0)
    highest_total_runs['100s'] = highest_total_runs['100s'].fillna(0)
    highest_total_runs['Innings Runs Scored Num'] = highest_total_runs['Innings Runs Scored Num'].astype(int)
    highest_total_runs['Innings Runs Scored'] = highest_total_runs['Innings Runs Scored'].astype(int)
    highest_total_runs['50s'] = highest_total_runs['50s'].astype(int)
    highest_total_runs['100s'] = highest_total_runs['100s'].astype(int)

    highest_total_runs.rename(
        columns={'Innings Runs Scored Num': 'Total Runs', 'Innings Runs Scored': 'Highest Scored'},
        inplace=True)
    highest_total_runs = highest_total_runs.sort_values(by='Total Runs', ascending=False).reset_index()
    # highest_total_runs.head()

    return highest_total_runs


def fetch_bowling_data(df):
    data = df
    # df.head()
    highest_total_wickets = data.groupby(['Innings Player', 'Country'])[
        ['4 Wickets', '5 Wickets', 'Innings Wickets Taken']].sum()
    highest_total_wickets.rename(
        columns={'Innings Wickets Taken': 'Total Wickets'},
        inplace=True)
    highest_total_wickets['Total Wickets'] = highest_total_wickets['Total Wickets'].fillna(0)
    highest_total_wickets['4 Wickets'] = highest_total_wickets['4 Wickets'].fillna(0)
    highest_total_wickets['5 Wickets'] = highest_total_wickets['5 Wickets'].fillna(0)
    highest_total_wickets['Total Wickets'] = highest_total_wickets['Total Wickets'].astype(int)
    highest_total_wickets['4 Wickets'] = highest_total_wickets['4 Wickets'].astype(int)
    highest_total_wickets['5 Wickets'] = highest_total_wickets['5 Wickets'].astype(int)

    # highest_total_wickets.rename(columns={'Innings Runs Scored': 'Highest Innings Runs Scored'}, inplace=True)
    highest_total_wickets = highest_total_wickets.sort_values(by='Total Wickets',
                                                              ascending=False).reset_index()
    # highest_total_wickets.head()

    return highest_total_wickets


def men_players_name(df):
    men_total_player_innings_stats = df
    men_player_name = men_total_player_innings_stats['Innings Player'].unique().tolist()
    men_player_name.sort()
    # men_player_name.insert(0, 'Overall')
    return men_player_name


def women_players_name(df):
    women_total_players_innings_stats = df
    women_player_name = women_total_players_innings_stats['Innings Player'].unique().tolist()
    women_player_name.sort()
    # women_player_name.insert(0, 'Overall')
    return women_player_name


def men_years_and_month(df, player_name):
    men_total_player_innings_stats = df
    filter_data = men_total_player_innings_stats[men_total_player_innings_stats['Innings Player'] == player_name]
    men_player_year = filter_data['Innings Year'].unique().tolist()
    men_player_year.sort()
    men_player_year.insert(0, "Overall")

    return men_player_year


def men_team(df):
    men_team_total_batting = df
    filter_data = men_team_total_batting['Team'].unique().tolist()
    filter_data.sort()
    return filter_data


def women_team(df):
    women_team_total_batting = df
    filter_data = women_team_total_batting['Team'].unique().tolist()
    filter_data.sort()
    return filter_data


def women_years_and_month(df, player_name):
    women_total_player_innings_stats = df
    filter_data = women_total_player_innings_stats[women_total_player_innings_stats['Innings Player'] == player_name]
    women_player_year = filter_data['Innings Year'].unique().tolist()
    women_player_year.sort()
    women_player_year.insert(0, "Overall")

    return women_player_year


def fetch_plot_batting(df, player, year):
    data = df
    if player != 'Overall' and year == 'Overall':
        # st.header(str(player) + " " + "Batting" + " " + 'Performance' + " " + 'Years')

        # plot the runs per year
        temp_batting_plot = data[data['Innings Player'] == player]
        # Create a grid of subplots with 1 row and 2 columns
        fig = make_subplots(rows=3, cols=2, subplot_titles=(
            "Runs Scored Per Year", "Average Per Year", "4s and 6s Per Year", "Runs Per Opposition", "Runs Per Ground",
            "50s and 100s Per Year"))

        # Plot the first bar chart - Runs Per Year
        group1 = temp_batting_plot.groupby('Innings Year')['Innings Runs Scored'].sum()
        fig.add_trace(go.Bar(x=group1.index, y=group1.values, name='Runs Scored'), row=1, col=1)
        fig.update_xaxes(title_text="Year", row=1, col=1)
        fig.update_yaxes(title_text="Runs", row=1, col=1)
        # fig.update_layout(title_text="Runs Scored Per Year")

        # Plot the second bar chart - Average Per Year
        group2 = temp_batting_plot.groupby('Innings Year')['Innings Batting Average'].mean()
        fig.add_trace(go.Bar(x=group2.index, y=group2.values, name='Batting Average'), row=1, col=2)
        fig.update_xaxes(title_text="Year", row=1, col=2)
        fig.update_yaxes(title_text="Average", row=1, col=2)
        # fig.update_layout(title_text="Average Per Year")

        # Plot the third line chart - 4s and 6s Per Year
        group3 = temp_batting_plot.groupby('Innings Year').agg(
            {'Innings Boundary Fours': 'sum', 'Innings Boundary Sixes': 'sum'})
        fig.add_trace(go.Scatter(x=group3.index, y=group3['Innings Boundary Fours'], mode='lines+markers', name='4s'),
                      row=2, col=1)
        fig.add_trace(go.Scatter(x=group3.index, y=group3['Innings Boundary Sixes'], mode='lines+markers', name='6s'),
                      row=2, col=1)
        fig.update_xaxes(title_text='Year', row=2, col=1)
        fig.update_yaxes(title_text='4s and 6s', row=2, col=1)
        # fig.update_layout(title_text="4s and 6s Per Year")

        group4 = temp_batting_plot.groupby('Opposition')['Innings Runs Scored'].sum()
        group4 = group4.sort_values(ascending=True)
        fig.add_trace(go.Bar(x=group4.values, y=group4.index, orientation='h', name='Runs against Opponent'), row=2,
                      col=2)
        fig.update_xaxes(title_text='Runs', row=2, col=2)
        # fig.update_yaxes(title_text='Opposition', row=2, col=2)
        # fig.update_layout(title_text="Runs Per Opposition")

        group5 = temp_batting_plot.groupby('Ground')['Innings Runs Scored'].sum()
        group5 = group5.sort_values(ascending=True)
        fig.add_trace(go.Bar(x=group5.values, y=group5.index, orientation='h', name='Runs in Ground'), row=3, col=1)
        fig.update_xaxes(title_text='Runs', row=3, col=1)

        group6 = temp_batting_plot.groupby('Innings Year').agg(
            {'50s': 'sum', '100s': 'sum'})
        fig.add_trace(go.Scatter(x=group6.index, y=group6['50s'], mode='lines+markers', name='50s'),
                      row=3, col=2)
        fig.add_trace(go.Scatter(x=group6.index, y=group6['100s'], mode='lines+markers', name='100s'),
                      row=3, col=2)
        fig.update_xaxes(title_text='Year', row=3, col=2)
        fig.update_yaxes(title_text='50s and 100s', row=3, col=2)

        fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')

        # Display the plotly figure in Streamlit
        st.plotly_chart(fig)
        return fig
    #
    elif player != 'Overall' and year != 'Overall':
        # st.header(str(player) + " " + "Batting" + " " + 'Performance' + " " + 'Month Wise')

        # plot the runs per year
        # temp_batting_plot = men_total_player_innings_stats[men_total_player_innings_stats['Innings Player'] == player]
        temp_batting_plot = data[
            (data['Innings Player'] == player) &
            (data['Innings Year'] == int(year))]
        # Create a grid of subplots with 1 row and 2 columns
        fig = make_subplots(rows=3, cols=2, subplot_titles=(
            "Runs Scored Per Month", "Average Per Month", "4s and 6s Per Month", "Runs Per Opposition",
            "Runs Per Ground",
            "50s and 100s Per Month"))

        # Plot the first bar chart - Runs Per Year
        group1 = temp_batting_plot.groupby('Innings Month')['Innings Runs Scored'].sum()
        fig.add_trace(go.Bar(x=group1.index, y=group1.values, name='Runs Scored'), row=1, col=1)
        fig.update_xaxes(title_text="Month", row=1, col=1)
        fig.update_yaxes(title_text="Runs", row=1, col=1)
        # fig.update_layout(title_text="Runs Scored Per Year")

        # Plot the second bar chart - Average Per Year
        group2 = temp_batting_plot.groupby('Innings Month')['Innings Batting Average'].mean()
        fig.add_trace(go.Bar(x=group2.index, y=group2.values, name='Batting Average'), row=1, col=2)
        fig.update_xaxes(title_text="Month", row=1, col=2)
        fig.update_yaxes(title_text="Average", row=1, col=2)
        # fig.update_layout(title_text="Average Per Year")

        # Plot the third line chart - 4s and 6s Per Year
        group3 = temp_batting_plot.groupby('Innings Month').agg(
            {'Innings Boundary Fours': 'sum', 'Innings Boundary Sixes': 'sum'})
        fig.add_trace(go.Scatter(x=group3.index, y=group3['Innings Boundary Fours'], mode='lines+markers', name='4s'),
                      row=2, col=1)
        fig.add_trace(go.Scatter(x=group3.index, y=group3['Innings Boundary Sixes'], mode='lines+markers', name='6s'),
                      row=2, col=1)
        fig.update_xaxes(title_text='Month', row=2, col=1)
        fig.update_yaxes(title_text='4s and 6s', row=2, col=1)
        # fig.update_layout(title_text="4s and 6s Per Year")

        group4 = temp_batting_plot.groupby(['Opposition', 'Innings Month'])['Innings Runs Scored'].sum()
        group4 = group4.sort_values(ascending=True)
        group4 = group4.reset_index()
        group4 = group4[['Opposition', 'Innings Runs Scored']]
        fig.add_trace(go.Bar(x=group4['Innings Runs Scored'], y=group4['Opposition'], orientation='h',
                             name='Runs against Opponent'), row=2, col=2)
        fig.update_xaxes(title_text='Runs', row=2, col=2)
        # fig.update_yaxes(title_text='Opposition', row=2, col=2)
        # fig.update_layout(title_text="Runs Per Opposition")

        group5 = temp_batting_plot.groupby(['Ground', 'Innings Month'])['Innings Runs Scored'].sum()
        group5 = group5.sort_values(ascending=True)
        group5 = group5.reset_index()
        group5 = group5[['Ground', 'Innings Runs Scored']]
        fig.add_trace(
            go.Bar(x=group5['Innings Runs Scored'], y=group5['Ground'], orientation='h', name='Runs Scored In Ground'),
            row=3, col=1)
        fig.update_xaxes(title_text='Runs', row=3, col=1)

        group6 = temp_batting_plot.groupby('Innings Month').agg(
            {'50s': 'sum', '100s': 'sum'})
        fig.add_trace(go.Scatter(x=group6.index, y=group6['50s'], mode='lines+markers', name='50s'),
                      row=3, col=2)
        fig.add_trace(go.Scatter(x=group6.index, y=group6['100s'], mode='lines+markers', name='100s'),
                      row=3, col=2)
        fig.update_xaxes(title_text='Month', row=3, col=2)
        fig.update_yaxes(title_text='50s and 100s', row=3, col=2)

        fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')

        # Display the plotly figure in Streamlit
        st.plotly_chart(fig)
        return fig


def fetch_plot_bowling(df, player, year):
    data = df
    if player != 'Overall' and year == 'Overall':
        # st.header(str(player) + " " + "Bowling" + " " + 'Performance' + " " + 'Years')

        # plot the runs per year
        temp_batting_plot = data[data['Innings Player'] == player]
        # Create a grid of subplots with 1 row and 2 columns
        fig = make_subplots(rows=3, cols=2, subplot_titles=(
            "Wicket Taken Per Year", "Bowling Average Per Year", "4 and 5 Wickets Per Year", "Wickets Per Opposition",
            "Wickets Per Ground",
            "Bowling Strike Rate Per Year"))

        # Plot the first bar chart - Runs Per Year
        group1 = temp_batting_plot.groupby('Innings Year')['Innings Wickets Taken'].sum()
        fig.add_trace(go.Bar(x=group1.index, y=group1.values, name='Wickets Taken'), row=1, col=1)
        fig.update_xaxes(title_text="Year", row=1, col=1)
        fig.update_yaxes(title_text="Wickets", row=1, col=1)
        # fig.update_layout(title_text="Runs Scored Per Year")

        # Plot the second bar chart - Average Per Year
        group2 = temp_batting_plot.groupby('Innings Year')['Innings Bowling Average'].mean()
        fig.add_trace(go.Bar(x=group2.index, y=group2.values, name='Bowling Average'), row=1, col=2)
        fig.update_xaxes(title_text="Year", row=1, col=2)
        fig.update_yaxes(title_text="Average", row=1, col=2)
        # fig.update_layout(title_text="Average Per Year")

        # Plot the third line chart - 4s and 6s Per Year
        group3 = temp_batting_plot.groupby('Innings Year').agg(
            {'4 Wickets': 'sum', '5 Wickets': 'sum'})
        fig.add_trace(go.Scatter(x=group3.index, y=group3['4 Wickets'], mode='lines+markers', name='4 Wickets'),
                      row=2, col=1)
        fig.add_trace(go.Scatter(x=group3.index, y=group3['5 Wickets'], mode='lines+markers', name='5 Wickets'),
                      row=2, col=1)
        fig.update_xaxes(title_text='Year', row=2, col=1)
        fig.update_yaxes(title_text='4 and 5 Wickets', row=2, col=1)
        # fig.update_layout(title_text="4s and 6s Per Year")

        group4 = temp_batting_plot.groupby('Opposition')['Innings Wickets Taken'].sum()
        group4 = group4.sort_values(ascending=True)
        fig.add_trace(go.Bar(x=group4.values, y=group4.index, orientation='h', name='Wickets Taken against Opposition'),
                      row=2, col=2)
        fig.update_xaxes(title_text='Wickets', row=2, col=2)
        # fig.update_yaxes(title_text='Opposition', row=2, col=2)
        # fig.update_layout(title_text="Runs Per Opposition")

        group5 = temp_batting_plot.groupby('Ground')['Innings Wickets Taken'].sum()
        group5 = group5.sort_values(ascending=True)
        fig.add_trace(go.Bar(x=group5.values, y=group5.index, orientation='h', name='Wickets Taken In Ground'), row=3,
                      col=1)
        fig.update_xaxes(title_text='Runs', row=3, col=1)

        group6 = temp_batting_plot.groupby('Innings Year')['Innings Bowling Strike Rate'].mean()
        fig.add_trace(go.Bar(x=group6.index, y=group6.values, name='Bowling Strike Rate'), row=3, col=2)
        fig.update_xaxes(title_text="Year", row=3, col=2)
        fig.update_yaxes(title_text="Strike Rate", row=3, col=2)

        fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')

        # fig.show()
        # Display the plotly figure in Streamlit
        st.plotly_chart(fig)
        return fig
    #
    elif player != 'Overall' and year != 'Overall':
        temp_batting_plot = data[
            (data['Innings Player'] == player) &
            (data['Innings Year'] == int(year))]
        # Create a grid of subplots with 1 row and 2 columns
        fig = make_subplots(rows=3, cols=2, subplot_titles=(
            "Wickets Taken Per Month", "Average Per Month", "4 and 5 Wickets Per Month", "Wickets Per Opposition",
            "Wickets Per Ground",
            "Bowling Strike Rate Per Month"))

        # Plot the first bar chart - Runs Per Year
        group1 = temp_batting_plot.groupby('Innings Month')['Innings Wickets Taken'].sum()
        fig.add_trace(go.Bar(x=group1.index, y=group1.values, name='Wickets Taken'), row=1, col=1)
        fig.update_xaxes(title_text="Month", row=1, col=1)
        fig.update_yaxes(title_text="Wickets", row=1, col=1)
        # fig.update_layout(title_text="Runs Scored Per Year")

        # Plot the second bar chart - Average Per Year
        group2 = temp_batting_plot.groupby('Innings Month')['Innings Bowling Average'].mean()
        fig.add_trace(go.Bar(x=group2.index, y=group2.values, name='Bowling Average'), row=1, col=2)
        fig.update_xaxes(title_text="Month", row=1, col=2)
        fig.update_yaxes(title_text="Average", row=1, col=2)
        # fig.update_layout(title_text="Average Per Year")

        # Plot the third line chart - 4s and 6s Per Year
        group3 = temp_batting_plot.groupby('Innings Month').agg(
            {'4 Wickets': 'sum', '5 Wickets': 'sum'})
        fig.add_trace(go.Scatter(x=group3.index, y=group3['4 Wickets'], mode='lines+markers', name='4 Wickets'),
                      row=2, col=1)
        fig.add_trace(go.Scatter(x=group3.index, y=group3['5 Wickets'], mode='lines+markers', name='5 Wickets'),
                      row=2, col=1)
        fig.update_xaxes(title_text='Month', row=2, col=1)
        fig.update_yaxes(title_text='4 and 5 Wickets', row=2, col=1)
        # fig.update_layout(title_text="4s and 6s Per Year")

        group4 = temp_batting_plot.groupby(['Opposition', 'Innings Month'])['Innings Wickets Taken'].sum()
        group4 = group4.sort_values(ascending=True)
        group4 = group4.reset_index()
        group4 = group4[['Opposition', 'Innings Wickets Taken']]
        fig.add_trace(go.Bar(x=group4['Innings Wickets Taken'], y=group4['Opposition'], orientation='h',
                             name='Wickets Taken against Opponent'), row=2, col=2)
        fig.update_xaxes(title_text='Wickets', row=2, col=2)
        # fig.update_yaxes(title_text='Opposition', row=2, col=2)
        # fig.update_layout(title_text="Runs Per Opposition")

        group5 = temp_batting_plot.groupby(['Ground', 'Innings Month'])['Innings Wickets Taken'].sum()
        group5 = group5.sort_values(ascending=True)
        group5 = group5.reset_index()
        group5 = group5[['Ground', 'Innings Wickets Taken']]
        fig.add_trace(go.Bar(x=group5['Innings Wickets Taken'], y=group5['Ground'], orientation='h',
                             name='Wickets Taken in Ground'), row=3, col=1)
        fig.update_xaxes(title_text='Wickets', row=3, col=1)

        group6 = temp_batting_plot.groupby('Innings Month')['Innings Bowling Strike Rate'].mean()
        fig.add_trace(go.Bar(x=group6.index, y=group6.values, name='Bowling Strike Rate'), row=3, col=2)
        fig.update_xaxes(title_text="Month", row=3, col=2)
        fig.update_yaxes(title_text="Strike Rate", row=3, col=2)

        fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')

        # Display the plotly figure in Streamlit
        st.plotly_chart(fig)
        return fig


def fetch_team_batting_plot(df1, df2, team):
    data1 = df1
    data2 = df2
    data1 = data1[data1['Team'] == team]
    data2 = data2[data2['Country'] == team]

    fig = make_subplots(rows=1, cols=5, specs=[
        [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'},
         {'type': 'indicator'}]], vertical_spacing=0.002)

    # Matches Played Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Mat'].iloc[0],
        title='Matches Played',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=1)

    # Matches Won Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Won'].iloc[0],
        title='Matches Won',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=2)

    # Matches Lost Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Lost'].iloc[0],
        title='Matches Lost',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=3)

    # Highest Scorecard
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['HS'].iloc[0],
        title='Highest Score',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=4)

    # Lowest Scorecard
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['LS'].iloc[0],
        title='Lowest Score',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=5)

    fig.update_layout(
        height=200,
        width=850
    )
    st.plotly_chart(fig)

    # fig = make_subplots(rows=2, cols=2, )
    fig = make_subplots(rows=3, cols=2, specs=[
        [{'type': 'bar'}, {'type': 'bar'}],
        [{'type': 'bar'}, {'type': 'bar'}],
        [{'type': 'bar'}, {'type': 'bar'}]
    ], subplot_titles=(
        "Most Runs", "Most 100s", "Most 6s and 4s", "Innings Played Vs Not Out", "Most Runs Against Opponent",
        "Most Runs In Ground"), vertical_spacing=0.3)

    group0 = data2.groupby('Innings Player').agg({'Innings Runs Scored Num': 'sum'})
    group0 = group0.sort_values(by='Innings Runs Scored Num', ascending=False)
    group0 = group0.reset_index()
    group0 = group0.head()
    fig.add_trace(go.Bar(x=group0['Innings Player'], y=group0['Innings Runs Scored Num'], name='Most Runs'), row=1,
                  col=1)
    # fig.update_xaxes(title_text="Player Name", row=1, col=1)
    fig.update_yaxes(title_text="Runs", row=1, col=1)

    # fig.add_trace(table_trace, row=1, col=1)

    # Plot the first bar chart - Runs Per Year
    group1 = data2.groupby('Innings Player')['100s'].sum()
    group1 = group1.sort_values(ascending=False)
    group1 = group1.reset_index()
    group1 = group1.head()
    fig.add_trace(go.Bar(x=group1['Innings Player'], y=group1['100s'], name='Most 100s'), row=1, col=2)
    # fig.update_xaxes(title_text="Player Name", row=1, col=1)
    fig.update_yaxes(title_text="100s", row=1, col=2)
    # fig.update_layout(title_text="Runs Scored Per Year")

    # Plot the second bar chart - Average Per Year
    group2 = data2.groupby('Innings Player')[['Innings Boundary Sixes', 'Innings Boundary Fours']].sum()
    group2 = group2.sort_values(by='Innings Boundary Sixes', ascending=False)
    group2 = group2.reset_index()
    group2 = group2.head()
    fig.add_trace(go.Bar(x=group2['Innings Player'], y=group2['Innings Boundary Sixes'], name='6s'), row=2, col=1)
    fig.add_trace(go.Bar(x=group2['Innings Player'], y=group2['Innings Boundary Fours'], name='4s'), row=2, col=1)
    # fig.update_xaxes(title_text="Player Name", row=1, col=2)
    fig.update_yaxes(title_text="Most 6s and 4s", row=2, col=1)
    # fig.update_layout(title_text="Average Per Year")

    group3 = data2.groupby('Innings Player').agg(
        {'Innings Batted Flag': 'sum', 'Innings Not Out Flag': 'sum'})
    group3 = group3.sort_values(by='Innings Not Out Flag', ascending=False)
    group3 = group3.reset_index()
    group3 = group3.head()
    fig.add_trace(go.Bar(x=group3['Innings Player'], y=group3['Innings Not Out Flag'], name='Not Out'), row=2, col=2)
    fig.add_trace(go.Scatter(x=group3['Innings Player'], y=group3['Innings Batted Flag'], mode='lines+markers',
                             name='Innings Batted Flag'),
                  row=2, col=2)
    fig.update_xaxes(title_text='Player Name', row=2, col=2)
    fig.update_yaxes(title_text='No. of Innings', row=2, col=2)

    group4 = data2.groupby(['Innings Player', 'Opposition'])['Innings Runs Scored Num'].sum()
    group4 = group4.reset_index()
    group4 = group4.sort_values(by='Innings Runs Scored Num', ascending=False)
    group4 = group4.head()
    # x_axis = [f"{player} vs {opposition}" for player, opposition in group4.index]

    x_axis = [f"{player} {opposition}" for player, opposition in zip(group4['Innings Player'], group4['Opposition'])]

    fig.add_trace(go.Bar(x=x_axis, y=group4['Innings Runs Scored Num'], name='Most Runs Against Opposition'), row=3,
                  col=1)
    fig.update_xaxes(title_text="Player vs Opposition", row=3, col=1)
    fig.update_yaxes(title_text="Runs Scored", row=3, col=1)

    group4 = data2.groupby(['Innings Player', 'Ground'])['Innings Runs Scored Num'].sum()
    group4 = group4.reset_index()
    group4 = group4.sort_values(by='Innings Runs Scored Num', ascending=False)
    group4 = group4.head()
    # x_axis = [f"{player} vs {opposition}" for player, opposition in group4.index]

    x_axis = [f"{player} in {ground}" for player, ground in zip(group4['Innings Player'], group4['Ground'])]

    fig.add_trace(go.Bar(x=x_axis, y=group4['Innings Runs Scored Num'], name='Most Runs in Ground'), row=3,
                  col=2)
    fig.update_xaxes(title_text="Player vs Ground", row=3, col=2)
    fig.update_yaxes(title_text="Runs Scored", row=3, col=2)

    fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')
    st.plotly_chart(fig)


def fetch_team_bowling_plot(df1, df2, team):
    data1 = df1
    data2 = df2
    data1 = data1[data1['Team'] == team]
    data2 = data2[data2['Country'] == team]

    fig = make_subplots(rows=1, cols=5, specs=[
        [{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'},
         {'type': 'indicator'}]])

    # Matches Played Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Mat'].iloc[0],
        title='Matches Played',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=1)

    # Matches Won Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Won'].iloc[0],
        title='Matches Won',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=2)

    # Matches Lost Card
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['Lost'].iloc[0],
        title='Matches Lost',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=3)

    # Highest Scorecard
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['HS'].iloc[0],
        title='Highest Score Conceded',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=4)

    # Lowest Scorecard
    fig.add_trace(go.Indicator(
        mode='number',
        value=data1['LS'].iloc[0],
        title='Lowest Score Conceded',
        number={'font': {'size': 45, 'color': '#f12617', 'family': 'Arial, sans-serif'}},
        align='center',
        title_font={
            'size': 15  # Increasing the title size  # Making the title bold
        },
    ), row=1, col=5)

    fig.update_layout(
        height=200,
        width=850
    )
    st.plotly_chart(fig)

    # fig = make_subplots(rows=2, cols=2, )
    fig = make_subplots(rows=2, cols=2, specs=[
        [{'type': 'bar'}, {'type': 'bar'}],
        [{'type': 'bar'}, {'type': 'bar'}]
    ], subplot_titles=(
        "Most Wickets", "Most 4 and 5 Wickets Haul", "Best Bowling Economy and Average",
        "Most Wicket against Opponent"))

    # Plot the first bar chart - Runs Per Year
    group1 = data2.groupby('Innings Player')['Innings Wickets Taken'].sum()
    group1 = group1.sort_values(ascending=False)
    group1 = group1.reset_index()
    group1 = group1.head()
    fig.add_trace(go.Bar(x=group1['Innings Player'], y=group1['Innings Wickets Taken'], name='Most Wickets'), row=1,
                  col=1)
    # fig.update_xaxes(title_text="Player Name", row=1, col=1)
    fig.update_yaxes(title_text="Wickets", row=1, col=1)
    # fig.update_layout(title_text="Runs Scored Per Year")

    # Plot the second bar chart - Average Per Year
    group2 = data2.groupby('Innings Player')[['4 Wickets', '5 Wickets']].sum()
    group2 = group2.sort_values(by='5 Wickets', ascending=False)
    group2 = group2.reset_index()
    group2 = group2.head()
    fig.add_trace(go.Bar(x=group2['Innings Player'], y=group2['4 Wickets'], name='4W'), row=1, col=2)
    fig.add_trace(go.Bar(x=group2['Innings Player'], y=group2['5 Wickets'], name='5W'), row=1, col=2)
    # fig.update_xaxes(title_text="Player Name", row=1, col=2)
    fig.update_yaxes(title_text="Most 4W and 5W", row=1, col=2)
    # fig.update_layout(title_text="Average Per Year")

    group3 = data2.groupby('Innings Player').agg(
        {'Innings Economy Rate': 'mean', 'Innings Bowling Average': 'mean'})
    group3 = group3.sort_values(by='Innings Economy Rate', ascending=False)
    group3 = group3.reset_index()
    group3 = group3.head()
    fig.add_trace(go.Scatter(x=group3['Innings Player'], y=group3['Innings Economy Rate'], mode='lines+markers',
                             name='Bowling Economy'), row=2, col=1)
    fig.add_trace(go.Scatter(x=group3['Innings Player'], y=group3['Innings Bowling Average'], mode='lines+markers',
                             name='Bowling Average'),
                  row=2, col=1)
    fig.update_xaxes(title_text='Player Name', row=2, col=1)
    fig.update_yaxes(title_text='Bowling Economy', row=2, col=1)

    group4 = data2.groupby(['Innings Player', 'Opposition'])['Innings Wickets Taken'].sum()
    group4 = group4.reset_index()
    group4 = group4.sort_values(by='Innings Wickets Taken', ascending=False)
    group4 = group4.head()
    # x_axis = [f"{player} vs {opposition}" for player, opposition in group4.index]

    x_axis = [f"{player} {opposition}" for player, opposition in zip(group4['Innings Player'], group4['Opposition'])]

    fig.add_trace(go.Bar(x=x_axis, y=group4['Innings Wickets Taken'], name='Most Wickets Against Opposition'), row=2,
                  col=2)
    fig.update_xaxes(title_text="Player vs Opposition", row=2, col=2)
    fig.update_yaxes(title_text="Wickets Taken", row=2, col=2)

    fig.update_layout(height=600, width=1000, showlegend=True, template='plotly_white')
    st.plotly_chart(fig)
