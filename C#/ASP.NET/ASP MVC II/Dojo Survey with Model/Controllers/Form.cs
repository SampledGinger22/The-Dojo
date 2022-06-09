using Microsoft.AspNetCore.Mvc;
namespace Dojo_Survey_With_Model.Controllers;
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