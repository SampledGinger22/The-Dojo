using Microsoft.AspNetCore.Mvc;
namespace Validating_Form_Submission.Controllers;
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult form()
        {
            
            return View();
        }
    }