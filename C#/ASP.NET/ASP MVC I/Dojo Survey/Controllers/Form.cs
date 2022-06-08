using Microsoft.AspNetCore.Mvc;
namespace Dojo_Survey.Controllers;
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult form()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }