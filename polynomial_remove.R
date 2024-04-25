library('dplyr')
library('ggplot2')
library('readr')
library('caret')
library('stringr')
options(digits = 22)

link = read_csv("C:/Users/ft7b6/Desktop/Year2_cut/pixel_geo_row_all_cotton.csv")



save_all_data =data.frame()


for (i in 1:120) {
  print(i)
  subset_data <- link[link$no_row == (i-1), ]
  quantiles <- quantile(subset_data$geo_y, probs = c(1/3, 2/3))
  
  part1 <- subset_data[subset_data$geo_y <= quantiles[1], ]
  part2 <- subset_data[(subset_data$geo_y > quantiles[1]) & (subset_data$geo_y <= quantiles[2]), ]
  part3 <- subset_data[subset_data$geo_y > quantiles[2], ]

  poly_remove <- function(part, i){
  model <- lm(geo_x ~ poly(geo_y, 5), data = part)
  pred <- predict(model, interval = "prediction", level = 0.9999)
  part_data = cbind(part, pred)
  weed = part_data[(part_data$lwr > part_data$geo_x) | (part_data$geo_x  > part_data$upr),]
  
  
  img <- ggplot(part, aes(geo_y, geo_x)) +
         geom_point() +
         geom_line(aes(y = pred[, "fit"]), color = "blue") +
         geom_ribbon(aes(ymin = pred[, "lwr"], ymax = pred[, "upr"]), alpha = 0.2, fill = "blue")
  ggsave(paste0("C:/Users/ft7b6/Desktop/Year2_cut/", i, '.png'), img, width = 10, height = 7)
  if(nrow(weed) != 0){
    new_part = part_data[-as.numeric(rownames(weed)),]
  }else{
    new_part = part_data
  }
  return(new_part)
  }
  non_weed_data = rbind(poly_remove(part1, i), poly_remove(part2, i), poly_remove(part3, i)) %>% select(-c('fit', 'lwr', 'upr'))
  save_all_data <- rbind(save_all_data, non_weed_data)
}
  
  
write_csv(save_all_data, "C:/Users/ft7b6/Desktop/Year2_cut/pixel_geo_row_weed_all_cotton.csv")
  
  
  
