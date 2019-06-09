library(ggplot2)
library(plotly)

shinyServer(function(input, output) {

  curv_init <- "test_180_120_"
  curv_mid <- "_"
  curv_end <- ".csv"
  
  c1 <- ""
  c2 <- ""
  c3 <- ""
  
  datos <- read.table(file="all_data.csv", sep = ",", header = TRUE)  
  
  
    
  output$migrafica <- renderPlot({
    
    # Valores curva 1
    if (input$curva1){
      error_1 <- input$error1
      est_1 <- input$estimacioninicial1
      # Error
      if (error_1 == 1) {
        c1_error <- "001"
      } else if (error_1 == 5) {
        c1_error <- "005"
      } else if (error_1 == 9) {
        c1_error <- "010"
      } else {
        cat ("Error inesperada")
      }
      # Estimation  
      if (est_1 == 0) {
        c1_est <- "0"
      } else if (est_1 == 2){
        c1_est <- "2"
      } else {
        cat ("Estimacion inesperada")
      }
      c1 <- paste0(curv_init,c1_error,curv_mid,c1_est,curv_end) 
    }

    # Valores curva 2
    if (input$curva2){
      error_2 <- input$error2
      est_2 <- input$estimacioninicial2
      # Error
      if (error_2 == 1) {
        c2_error <- "001"
      } else if (error_2 == 5) {
        c2_error <- "005"
      } else if (error_2 == 9) {
        c2_error <- "010"
      } else {
        cat ("Error inesperada")
      }
      # Estimation  
      if (est_2 == 0) {
        c2_est <- "0"
      } else if (est_2 == 2){
        c2_est <- "2"
      } else {
        cat ("Estimacion inesperada")
      }
      c2 <- paste0(curv_init,c2_error,curv_mid,c2_est,curv_end) 
    }

    # Valores curva 3
    if (input$curva3){
      error_3 <- input$error3
      est_3 <- input$estimacioninicial3
      # Error
      if (error_3 == 1) {
        c3_error <- "001"
      } else if (error_3 == 5) {
        c3_error <- "005"
      } else if (error_3 == 9) {
        c3_error <- "010"
      } else {
        cat ("Error inesperada")
      }
      # Estimation  
      if (est_3 == 0) {
        c3_est <- "0"
      } else if (est_3 == 2){
        c3_est <- "2"
      } else {
        cat ("Estimacion inesperada")
      }
      c3 <- paste0(curv_init,c3_error,curv_mid,c3_est,curv_end) 
    }    
            
    datos_sub=subset(datos,case %in% c(c1,c2,c3))
    
    qplot(iter,reward, data = datos_sub,geom="line",color=case) 
    
  })
  
})