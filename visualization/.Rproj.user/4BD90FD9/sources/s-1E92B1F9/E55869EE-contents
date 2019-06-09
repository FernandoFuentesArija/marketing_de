library(ggplot2)
library(plotly)

shinyUI(
  fluidPage(
    titlePanel("Curvas de recompensa para 120 agentes en 180 interacciones"),
    sidebarLayout(
      sidebarPanel(
        
        checkboxInput("curva1", label = "Curva 1", value = TRUE),
        sliderInput("error1",
                    label="Error primera curva",
                    min = 1, max = 9, value = 1, step = 4),
        sliderInput("estimacioninicial1",
                    label="Estimacion inicial primera curva",
                    min = 0, max = 2, value = 0, step = 2),
        
        checkboxInput("curva2", label = "Curva 2", value = TRUE),
        sliderInput("error2",
                    label="Error segunda curva",
                    min = 1, max = 9, value = 5, step = 4),
        sliderInput("estimacioninicial2",
                    label="Estimacion inicial segunda curva",
                    min = 0, max = 2, value = 0, step = 2),
        
        checkboxInput("curva3", label = "Curva 3", value = TRUE),
        sliderInput("error3",
                    label="Error tercera curva",
                    min = 1, max = 9, value = 1, step = 4),
        sliderInput("estimacioninicial3",
                    label="Estimacion inicial tercera curva",
                    min = 0, max = 2, value = 2, step = 2)
        
      ),
      mainPanel(
        plotOutput("migrafica")
      )
    )
  )
)