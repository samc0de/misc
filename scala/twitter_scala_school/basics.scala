def aFunction(param: String) = {  // Multi-statement func in {}.
  println("Inside 'aFunction', got '" + param + "' as parameter.")
}  // String addition with vars/params.


def addOne(m: Int): Int = m + 1  // camelCase. Oneliner. No need to type return.

val anonymousFunc = () => {  // Unspecified return type = Unit.
  println("Inside an anonymous function, ofcource we'll have a name bound for it via 'val' assignment.")
}

// val anotherAnonymousFunc = (): String => {  // return type gives error.
val anotherAnonymousFunc = () => {  // No inputs.
  println("Inside another anonymous function, ofcource we'll have a name for it.")
  "Return Value!"  // This is the return value, but no return type specified.
}


var counter = 0  // Var can change, val = const, can't.

val count = () => counter = counter + 1  // No i/p or o/p.


// Partial functions.


def add(m: Int, n: Int): Int = m + n

var addTwo = add(2, _: Int)

def addThree(r: Double): Int = r.intValue + 3  // This is not partial.


// Curried functions.


// Return type doesn't always need to be defined.
def totalPrice(vat: Double)(serviceTax: Double)(mrp: Double): Double = {
  println("MRP is: " + mrp)
  println("Service Tax is: " + serviceTax + " %")
  println("VAT is: " + vat + " %")
  mrp + mrp * serviceTax/100 + mrp * vat/100
}

// val fixedVatApplied = totalPrice(15) _
// vatApplied
def vatApplier(vat: Double) = {  // Not specifying return type.
  println("Pre applying VAT rate of: " + vat + " %")
  totalPrice(vat) _
}

def vatSTApplier(serviceTax: Double) = vatApplier(serviceTax) _

def taxesApplier(vat: Double)(serviceTax: Double) = totalPrice(vat)(serviceTax) _
