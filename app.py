import streamlit as st
import preprocessor, helper

men_total_player_innings_stats = preprocessor.men_total_player_innings_stats
men_test_player_innings_stats = preprocessor.men_test_player_innings_stats
men_odi_player_innings_stats = preprocessor.men_odi_player_innings_stats
men_t20_player_innings_stats = preprocessor.men_t20_player_innings_stats

women_total_player_innings_stats = preprocessor.women_total_player_innings_stats
women_test_player_innings_stats = preprocessor.women_test_player_innings_stats
women_odi_player_innings_stats = preprocessor.women_odi_player_innings_stats
women_t20_player_innings_stats = preprocessor.women_t20_player_innings_stats

men_team_total_batting = preprocessor.men_team_total_batting
men_team_total_bowling = preprocessor.men_team_total_bowling
men_test_team_batting = preprocessor.men_test_team_batting
men_test_team_bowling = preprocessor.men_test_team_bowling
men_odi_team_batting = preprocessor.men_odi_team_batting
men_odi_team_bowling = preprocessor.men_odi_team_bowling
men_t20_team_batting = preprocessor.men_t20_team_batting
men_t20_team_bowling = preprocessor.men_t20_team_bowling

women_team_total_batting = preprocessor.women_team_total_batting
women_team_total_bowling = preprocessor.women_team_total_bowling
women_test_team_batting = preprocessor.women_test_team_batting
women_test_team_bowling = preprocessor.women_test_team_bowling
women_odi_team_batting = preprocessor.women_odi_team_batting
women_odi_team_bowling = preprocessor.women_odi_team_bowling
women_t20_team_batting = preprocessor.women_t20_team_batting
women_t20_team_bowling = preprocessor.women_t20_team_bowling

st.sidebar.title('World Cricket Analysis')
st.sidebar.image("images.png", width=230)

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Runs and Wickets', 'Player Performance', 'Team Performance')
)
user_gender = st.sidebar.radio(
    'Select an Gender',
    ('Men', 'Women'),
)

user_format = st.sidebar.radio('Select an Format', options=['All', 'Test', 'ODI', 'T20'])

user_option = st.sidebar.radio('Select an Batting or Bowling', options=['Batting', 'Bowling'])

# st.dataframe(df)
if user_menu == 'Runs and Wickets':
    if user_gender == 'Men' and user_format == 'All' and user_option == 'Batting':
        st.header('Most Runs in All Format')
        men_total_runs = helper.fetch_batting_data(men_total_player_innings_stats)
        men_total_runs = men_total_runs.head(25)
        st.table(men_total_runs)
    elif user_gender == 'Men' and user_format == 'All' and user_option == 'Bowling':
        st.header('Most Wickets in All Format')
        men_total_wickets = helper.fetch_bowling_data(men_total_player_innings_stats)
        men_total_wickets = men_total_wickets.head(25)
        st.table(men_total_wickets)

    elif user_gender == 'Men' and user_format == 'Test' and user_option == 'Batting':
        st.header('Most Runs in Test Format')
        men_total_test_runs = helper.fetch_batting_data(men_test_player_innings_stats)
        men_total_test_runs = men_total_test_runs.head(25)
        st.table(men_total_test_runs)
    elif user_gender == 'Men' and user_format == 'Test' and user_option == 'Bowling':
        st.header('Most Wickets in Test')
        men_total_test_wickets = helper.fetch_bowling_data(men_test_player_innings_stats)
        men_total_test_wickets = men_total_test_wickets.head(25)
        st.table(men_total_test_wickets)

    elif user_gender == 'Men' and user_format == 'ODI' and user_option == 'Batting':
        st.header('Most Runs in ODI Format')
        men_total_odi_runs = helper.fetch_batting_data(men_odi_player_innings_stats)
        men_total_odi_runs = men_total_odi_runs.head(20)
        st.table(men_total_odi_runs)
    elif user_gender == 'Men' and user_format == 'ODI' and user_option == 'Bowling':
        st.header('Most Wickets in ODI')
        men_total_odi_wickets = helper.fetch_bowling_data(men_odi_player_innings_stats)
        men_total_odi_wickets = men_total_odi_wickets.head(25)
        st.table(men_total_odi_wickets)

    elif user_gender == 'Men' and user_format == 'T20' and user_option == 'Batting':
        st.header('Most Runs in T20 Format')
        men_total_t20_runs = helper.fetch_batting_data(men_t20_player_innings_stats)
        men_total_t20_runs = men_total_t20_runs.head(25)
        st.table(men_total_t20_runs)
    elif user_gender == 'Men' and user_format == 'T20' and user_option == 'Bowling':
        st.header('Most Wickets in T20 Format')
        men_total_t20_wickets = helper.fetch_bowling_data(men_t20_player_innings_stats)
        men_total_t20_wickets = men_total_t20_wickets.head(25)
        st.table(men_total_t20_wickets)

    elif user_gender == 'Women' and user_format == 'All' and user_option == 'Batting':
        st.header('Most Runs in Women All Format')
        women_total_runs = helper.fetch_batting_data(women_total_player_innings_stats)
        women_total_runs = women_total_runs.head(25)
        st.table(women_total_runs)
    elif user_gender == 'Women' and user_format == 'All' and user_option == 'Bowling':
        st.header('Most Wickets in Women All Format')
        women_total_wickets = helper.fetch_bowling_data(women_total_player_innings_stats)
        women_total_wickets = women_total_wickets.head(25)
        st.table(women_total_wickets)

    elif user_gender == 'Women' and user_format == 'Test' and user_option == 'Batting':
        st.header('Most Runs in Women Test Format')
        women_total_test_runs = helper.fetch_batting_data(women_test_player_innings_stats)
        women_total_test_runs = women_total_test_runs.head(25)
        st.table(women_total_test_runs)
    elif user_gender == 'Women' and user_format == 'Test' and user_option == 'Bowling':
        st.header('Most Wickets in Women Test Format')
        women_total_test_wickets = helper.fetch_bowling_data(women_test_player_innings_stats)
        women_total_test_wickets = women_total_test_wickets.head(25)
        st.table(women_total_test_wickets)

    elif user_gender == 'Women' and user_format == 'ODI' and user_option == 'Batting':
        st.header('Most Runs in Women ODI Format')
        women_total_odi_runs = helper.fetch_batting_data(women_odi_player_innings_stats)
        women_total_odi_runs = women_total_odi_runs.head(25)
        st.table(women_total_odi_runs)
    elif user_gender == 'Women' and user_format == 'ODI' and user_option == 'Bowling':
        st.header('Most Wickets in Women ODI Format')
        women_total_odi_wickets = helper.fetch_bowling_data(women_odi_player_innings_stats)
        women_total_odi_wickets = women_total_odi_wickets.head(25)
        st.table(women_total_odi_wickets)

    elif user_gender == 'Women' and user_format == 'T20' and user_option == 'Batting':
        st.header('Most Runs in Women T20 Format')
        women_total_t20_runs = helper.fetch_batting_data(women_t20_player_innings_stats)
        women_total_t20_runs = women_total_t20_runs.head(25)
        st.table(women_total_t20_runs)
    elif user_gender == 'Women' and user_format == 'T20' and user_option == 'Bowling':
        st.header('Most Wickets in Women T20 Format')
        women_total_t20_wickets = helper.fetch_bowling_data(women_t20_player_innings_stats)
        women_total_t20_wickets = women_total_t20_wickets.head(25)
        st.table(women_total_t20_wickets)

if user_menu == 'Player Performance':

    if user_gender == 'Men' and user_option == 'Batting' and user_format == 'All':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " " + "Batting" + " " + 'Performance')
        temp_batting_df = helper.fetch_plot_batting(men_total_player_innings_stats, men_selected_player,
                                                    men_selected_year)
    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'All':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)
        st.header(str(men_selected_player) + " " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(men_total_player_innings_stats, men_selected_player,
                                                    men_selected_year)
    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'Test':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)
        st.header(str(men_selected_player) + " Test " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(men_test_player_innings_stats, men_selected_player,
                                                    men_selected_year)
    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'Test':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " Test " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(men_test_player_innings_stats, men_selected_player,
                                                    men_selected_year)

    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'ODI':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " ODI " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(men_odi_player_innings_stats, men_selected_player,
                                                    men_selected_year)

    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'ODI':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('SR Tendulkar'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " ODI " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(men_odi_player_innings_stats, men_selected_player,
                                                    men_selected_year)
    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'T20':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('V Kohli'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " T20 " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(men_t20_player_innings_stats, men_selected_player,
                                                    men_selected_year)
    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'T20':
        men_player = helper.men_players_name(men_total_player_innings_stats)
        men_selected_player = st.sidebar.selectbox('Select Player', men_player, index=men_player.index('JJ Bumrah'))

        men_years = helper.men_years_and_month(men_total_player_innings_stats, men_selected_player)
        # # get the selected index
        men_selected_player_index = men_player.index(men_selected_player)

        men_selected_year = st.sidebar.selectbox('Select Year', men_years)

        st.header(str(men_selected_player) + " T20 " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(men_t20_player_innings_stats, men_selected_player,
                                                    men_selected_year)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'All':
        women_player = helper.women_players_name(women_total_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_total_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " Overall " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(women_total_player_innings_stats, women_selected_player,
                                                    women_selected_year)
    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'All':
        women_player = helper.women_players_name(women_total_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_total_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " Overall " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(women_total_player_innings_stats, women_selected_player,
                                                    women_selected_year)
    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'Test':
        women_player = helper.women_players_name(women_test_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_test_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " Test " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(women_test_player_innings_stats, women_selected_player,
                                                    women_selected_year)
    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'Test':
        women_player = helper.women_players_name(women_test_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_test_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " Test " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(women_test_player_innings_stats, women_selected_player,
                                                    women_selected_year)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'ODI':
        women_player = helper.women_players_name(women_odi_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_odi_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " ODI " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(women_odi_player_innings_stats, women_selected_player,
                                                    women_selected_year)

    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'ODI':
        women_player = helper.women_players_name(women_odi_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_odi_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " ODI " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(women_odi_player_innings_stats, women_selected_player,
                                                    women_selected_year)
    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'T20':
        women_player = helper.women_players_name(women_t20_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_t20_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " T20 " + "Batting " + "Performance ")

        temp_batting_df = helper.fetch_plot_batting(women_t20_player_innings_stats, women_selected_player,
                                                    women_selected_year)

    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'T20':
        women_player = helper.women_players_name(women_total_player_innings_stats)
        women_selected_player = st.sidebar.selectbox('Select Player', women_player,
                                                     index=women_player.index('EA Perry'))

        women_years = helper.women_years_and_month(women_t20_player_innings_stats, women_selected_player)
        # # get the selected index
        women_selected_player_index = women_player.index(women_selected_player)

        women_selected_year = st.sidebar.selectbox('Select Year', women_years)

        st.header(str(women_selected_player) + " T20 " + "Bowling " + "Performance ")

        temp_batting_df = helper.fetch_plot_bowling(women_t20_player_innings_stats, women_selected_player,
                                                    women_selected_year)

if user_menu == 'Team Performance':

    if user_gender == 'Men' and user_option == 'Batting' and user_format == 'All':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)
        st.header(str(men_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance')

        temp_batting_df = helper.fetch_team_batting_plot(men_team_total_batting, men_total_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'All':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance')

        temp_batting_df = helper.fetch_team_bowling_plot(men_team_total_bowling, men_total_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'Test':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "Test")

        temp_batting_df = helper.fetch_team_batting_plot(men_test_team_batting, men_test_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'Test':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "Test")

        temp_batting_df = helper.fetch_team_bowling_plot(men_test_team_bowling, men_test_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'ODI':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "ODI")

        temp_batting_df = helper.fetch_team_batting_plot(men_odi_team_batting, men_odi_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'ODI':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "ODI")

        temp_batting_df = helper.fetch_team_bowling_plot(men_odi_team_bowling, men_odi_player_innings_stats,
                                                         men_selected_team)
    elif user_gender == 'Men' and user_option == 'Batting' and user_format == 'T20':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "T20")

        temp_batting_df = helper.fetch_team_batting_plot(men_t20_team_batting, men_t20_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Men' and user_option == 'Bowling' and user_format == 'T20':
        men_team = helper.men_team(men_team_total_batting)
        men_selected_team = st.sidebar.selectbox('Select Team', men_team)

        st.header(str(men_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "T20")

        temp_batting_df = helper.fetch_team_bowling_plot(men_t20_team_bowling, men_t20_player_innings_stats,
                                                         men_selected_team)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'All':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "Overall")

        temp_batting_df = helper.fetch_team_batting_plot(women_team_total_batting, women_test_player_innings_stats,
                                                         women_selected_team)
    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'All':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "Overall")

        temp_batting_df = helper.fetch_team_bowling_plot(women_team_total_bowling, women_test_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'Test':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "Test")

        temp_batting_df = helper.fetch_team_batting_plot(women_test_team_batting, women_test_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'Test':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "Test")

        temp_batting_df = helper.fetch_team_bowling_plot(women_test_team_bowling, women_test_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'ODI':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "ODI")

        temp_batting_df = helper.fetch_team_batting_plot(women_odi_team_batting, women_odi_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'ODI':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "ODI")

        temp_batting_df = helper.fetch_team_bowling_plot(women_odi_team_bowling, women_odi_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Batting' and user_format == 'T20':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Batting" + " " + 'Performance ' + "In " + "T20")

        temp_batting_df = helper.fetch_team_batting_plot(women_t20_team_batting, women_t20_player_innings_stats,
                                                         women_selected_team)

    elif user_gender == 'Women' and user_option == 'Bowling' and user_format == 'T20':

        women_team = helper.women_team(women_team_total_batting)
        women_selected_team = st.sidebar.selectbox('Select Team', women_team)

        st.header(str(women_selected_team) + " " + "Team" + " " + "Bowling" + " " + 'Performance ' + "In " + "T20")

        temp_batting_df = helper.fetch_team_bowling_plot(women_t20_team_bowling, women_t20_player_innings_stats,
                                                         women_selected_team)
