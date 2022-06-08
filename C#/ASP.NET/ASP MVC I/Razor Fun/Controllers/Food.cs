using Microsoft.AspNetCore.Mvc;
namespace readingimplimentation.Controllers;     //be sure to use your own project's namespace!
    public class HomeController : Controller   //remember inheritance??
    {
        //for each route this controller is to handle:
        [HttpGet("")]       //type of request
        public ViewResult Foods()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }