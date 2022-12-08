hydropower_plants_US <- read.csv("hydropower_plants_US.csv")

View(hydropower_plants_US)

hydropower_plants_US_new <- aggregate(cbind(count = State) ~ State, 
          data = hydropower_plants_US, 
          FUN = function(x){NROW(x)})

str(hydropower_plants_US_new)

hydropower_plants_US_new <- hydropower_plants_US_new[order(hydropower_plants_US_new$count),]

ggplot(hydropower_plants_US_new, aes(x = reorder(State, count), y = count, fill = State)) + xlab("State") + ylab("Number of Hydropower Plants") +
  geom_bar(stat="identity") + theme_minimal() + scale_fill_manual(values = rep(c("#c45c5c", "#73a7cc", "#55a599", "#f2bc7d", "#ab83c4", "#ec8958", "#e178b2", "#80ca95", "#8081d4", "#ac5381"),5)) + theme(legend.position = "none")

summary(hydropower_plants_US_new$count)

us_census_median_household_income <- read.csv("ACSST5Y2020.S1903-Data.csv")

require(dplyr)
require(ggplot2)

us_census_median_household_income <- us_census_median_household_income %>% dplyr::select(2, 323)

View(us_census_median_household_income)

us_census_median_household_income <- us_census_median_household_income[-1,]

colnames(us_census_median_household_income) = c("State", "Income")

us_census_median_household_income$Income <- as.numeric(us_census_median_household_income$Income)

str(us_census_median_household_income)

summary(us_census_median_household_income$Income)

us_census_median_household_income <- us_census_median_household_income[order(us_census_median_household_income$Income),]

ggplot(us_census_median_household_income, aes(x = reorder(State, Income), y = Income, fill = State)) + xlab("State") + ylab("Income") +
  geom_bar(stat="identity") + theme_minimal() + scale_fill_manual(values = rep(c("#c45c5c", "#73a7cc", "#55a599", "#f2bc7d", "#ab83c4", "#ec8958", "#e178b2", "#80ca95", "#8081d4", "#ac5381"),6)) + theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust=1))


population <- read.csv("precipitation_average_per_state.csv")

population <- population %>% dplyr::select(3, 5)

population$Population <- as.numeric(gsub(',', '', population$Population))

population <- population[order(population$Population),]

ggplot(population, aes(x = reorder(StateAbbreviations, Population), y = Population, fill = StateAbbreviations)) + xlab("State") + ylab("Population") +
  geom_bar(stat="identity") + theme_minimal() + scale_fill_manual(values = rep(c("#c45c5c", "#73a7cc", "#55a599", "#f2bc7d", "#ab83c4", "#ec8958", "#e178b2", "#80ca95", "#8081d4", "#ac5381"),6)) + theme(legend.position = "none")

summary(population$Population)
