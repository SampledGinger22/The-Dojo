using Microsoft.AspNetCore.Mvc;
namespace Portolio_II.Controllers;
    public class HomeController : Controller
    {
        [HttpGet("")]
        public ViewResult landing()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }

