install.packages("Ckmeans.1d.dp")
install.packages("RColorBrewer")

require(RColorBrewer)
require(Ckmeans.1d.dp)

# https://cran.r-project.org/web/packages/Ckmeans.1d.dp/vignettes/Ckmeans.1d.dp.html

precipitation_data <- read.csv("precipitation_data_final.csv")

View(precipitation_data)

precipitation_data_condensed <- precipitation_data$avg

###

# Initialize total within sum of squares error: wss
wss <- 0

# For 1 to 15 cluster centers
for (i in 1:10) {
  km.out <- Ckmeans.1d.dp(precipitation_data_condensed, i)
  # Save total within sum of squares to wss variable
  wss[i] <- km.out$tot.withinss
}

# Plot total within sum of squares vs. number of clusters
plot(1:10, wss, type = "b", 
     xlab = "Number of Clusters", 
     ylab = "Within groups sum of squares")

###

# Clustering
library(cluster)
library(factoextra)

df <- data.frame(precipitation_data_condensed)

silhouette_score <- function(k){
  km <- Ckmeans.1d.dp(precipitation_data_condensed, k)
  ss <- silhouette(km$cluster, dist(df))
  mean(ss)
}
k <- 1:10
avg_sil <- sapply(k, silhouette_score)
plot(k, type='b', avg_sil, xlab='Number of clusters', ylab='Average Silhouette Scores', frame=FALSE)

fviz_nbclust(df, kmeans, method='silhouette')

###

k <- 3

result <- Ckmeans.1d.dp(precipitation_data_condensed, k)

result$cluster

colors <- brewer.pal(5, "Dark2")
plot(result, col.clusters = colors)

plot(precipitation_data_condensed, col=colors[result$cluster], pch=result$cluster, cex=1.5,
     main="Optimal univariate clustering given k",
     sub=paste("Number of clusters given:", k))
abline(h=result$centers, col=colors, lty="dashed", lwd=2)
legend("bottomright", paste("Cluster", 1:k), col=colors, pch=1:k, cex=1, bty="n")

precipitation_data$cluster = result$cluster

cluster_1 <- precipitation_data[precipitation_data$cluster == 1,]
cluster_2 <- precipitation_data[precipitation_data$cluster == 2,]
cluster_3 <- precipitation_data[precipitation_data$cluster == 3,]
cluster_4 <- precipitation_data[precipitation_data$cluster == 4,]
cluster_5 <- precipitation_data[precipitation_data$cluster == 5,]

write.csv(cluster_1, "cluster_1.csv")
write.csv(cluster_2, "cluster_2.csv")
write.csv(cluster_3, "cluster_3.csv")
write.csv(cluster_4, "cluster_4.csv")
write.csv(cluster_5, "cluster_5.csv")

result$centers

florida <- precipitation_data[precipitation_data$state == "Florida",]

mean(florida$avg)

max(florida$avg)

brewer.pal(n = 8, name = "Dark2")

ggplot(data = precipitation_data, aes(x=state, y=avg, fill=state)) + theme_minimal() + scale_fill_manual(values = c("#c45c5c", "#73a7cc", "#55a599", "#f2bc7d", "#ab83c4", "#ec8958", "#e178b2", "#80ca95", "#8081d4", "#ac5381")) + geom_boxplot() + theme(legend.position = "none", axis.text.x = element_text(angle = 45, hjust=1))

hist(precipitation_data$avg)

summary(precipitation_data$avg)
