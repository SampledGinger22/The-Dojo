class Queue {
    constructor(items = []) {
      this.items = items;
    }
    // add methods here, outside constructor
    newMethod(params) {
      // 'this' keyword will refer to the class instance
      // that newMethod was called on
    }
  }
  
  class Stack {
    constructor(items = []) {
      this.items = items;
    }
    // add methods here, outside constructor
    newMethod(params) {
      // 'this' keyword will refer to the class instance
      // that newMethod was called on
    }
  }
  
  // Alternate way to add method to class
  NameOfClass.prototype.newMethodsName = function (params) {
    // 'this' keyword inside method
    // will refer to the class instance that
    // the newMethod was called on
  };