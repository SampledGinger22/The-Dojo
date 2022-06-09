using Microsoft.AspNetCore.Mvc;
using Dojo_Survey_with_Validation.Models;
namespace Dojo_Survey_with_Validation.Controllers;
    public class HomeFormReturn : Controller
    {
        [HttpPost("result")]
        public IActionResult formreturn(Ninja ninja){
            return View("formreturn", ninja);
        }
    }