using Microsoft.AspNetCore.Mvc;
namespace Dojo_Survey_with_Validation.Controllers;
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult form()
        {
            //Views/Home/HiThere.cshtml
            //Views/Shared/HiThere.cshtml
            return View();
        }
    }