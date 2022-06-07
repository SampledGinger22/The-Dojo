using Microsoft.AspNetCore.Mvc;
namespace PortfolioI.Controllers;     //be sure to use your own project's namespace!

public class Index : Controller{


    [HttpGet]
    [Route("")]
    public string MyIndex(){
        return "This is my Index!";
    }
}