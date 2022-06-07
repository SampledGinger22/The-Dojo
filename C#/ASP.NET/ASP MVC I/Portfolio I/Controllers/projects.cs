using Microsoft.AspNetCore.Mvc;
namespace PortfolioI.Controllers;     //be sure to use your own project's namespace!

public class Projects : Controller{


    [HttpGet]
    [Route("/projects")]
    public string MyProjects(){
        return "These are my projects";
    }
}