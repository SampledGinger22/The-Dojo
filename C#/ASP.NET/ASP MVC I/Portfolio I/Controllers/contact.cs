using Microsoft.AspNetCore.Mvc;
namespace PortfolioI.Controllers;     //be sure to use your own project's namespace!

public class Contacts : Controller{


    [HttpGet]
    [Route("/contact")]
    public string MyContact(){
        return "This is my Contact!";
    }
}