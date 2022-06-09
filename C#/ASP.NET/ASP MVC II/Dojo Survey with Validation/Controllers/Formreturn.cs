using Microsoft.AspNetCore.Mvc;
using Dojo_Survey_with_Validation.Models;
namespace Dojo_Survey_with_Validation.Controllers;
    public class SharedController : Controller
    {
        [HttpPost("result")]
        public IActionResult formreturn(Ninja ninja){
            
            if(ModelState.IsValid)
            {
                return View("formreturn", ninja);   
            }
            else 
            {
                return View("form");
            }
        }
    }