<p align="center">
  <a href="https://sriley.dev"><img src="./GHBanner_v3.png" width="65%"></a>
<br>
  <hr>
  <!-- [![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=I'm+a+student+at+Montana+State;Second+line+of+text)](https://git.io/typing-svg)
 -->
<a href="https://www.buymeacoffee.com/pharaohcola13"><img src="https://github.com/k4m4/donations/blob/master/images/badge.svg" alt="Donations Badge" height="28"></a>&nbsp;&nbsp;
<a href="https://board.sriley.dev" target="_blank"><img src="https://img.shields.io/badge/My%20Dev%20Board-007AC0?style=for-the-badge&logo=Trello&logoColor=white"></a>
  <a href="https://sriley.dev">
    <img src="https://img.shields.io/badge/website%20-%234285F4.svg?&style=for-the-badge&logo=chrome&logoColor=white"/>
  </a>&nbsp;&nbsp;
  <a href="https://rgate.sriley.dev">
   <img height="32" width="32" src="https://cdn.simpleicons.org/Researchgate/00CCBB" />
  </a>&nbsp;&nbsp;
  <a href="https://orcid.org/0000-0001-7949-9163">
    <img height="32" width="32" src="https://cdn.simpleicons.org/Orcid/A6CE39" />
  </a>
</div>

```R
  #> author: Spencer Riley <academic@sriley.dev>
  #> website: https://sriley.dev
  #> trello: https://board.sriley.dev
  about.me <- function(...){
    Languages <- c("Python", "R", "LaTeX", "JavaScript", "HTML", "Flutter", "C", "IDL")
    FrameWorks <- c("Docker", "Jupyter", "Kubernetes")
    CI <- c("GitHub Actions")

    currently.learning <- "Numerical simulation methods to study magnetohydrodynamics."

    goals.completed <- goals.todo <- list()
       
    if (Sys.date() > as.POSIXct("2023-01-01")) {
      goals.todo <- append(goals.todo, "Find some good recipes")
      goals.todo <- append(goals.todo, "Pass my Qualifying Exams")
      goals.todo <- append(goals.todo, "Finish PMAT V3.0 (Guess I didn't finish this yet)")
      
      # Paper draft is available https://github.com/physicsgoddess1972/Precipitable-Water-Model/blob/paper/paper.pdf
      goals.todo <- append(goals.todo, "Finish a paper for the Journal of Open Source Software")
    }

    goals.completed <- append(goals.completed, "Get into graduate school")
    # Paper is available at https://doi.org/10.5194/amt-15-1563-2022
    goals.completed <- append(goals.completed, "Published first paper")

    fun.fact <- "My favorate animal is the whale shark"
  }
  
  about.me()
  
```
