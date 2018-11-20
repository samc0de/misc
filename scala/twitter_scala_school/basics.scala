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


// Variable length args.
def capitalizeAll(args: String*) = {
  args.map(arg => arg.capitalize)
}


// Classes and objects.
class CasioCalculator {
  var brand: String = "Casio"
  def add (m: Int, n: Int) = a + b
}

// Class with a constructor.
class Calculator(brand: String) {  // brand is not stored, unless explicitly done.
  /**
   * A Constructor.
   */  // Note comment styles, like c++.
  val colour: String = if (brand == "CASIO") {  // Expression.
    "blue"
  } else if (brand == "HP") {
    "green"
  } else if (brand == "TI") {
    "black"
  } else "white"
  def add(a: Double, b: Double): Double = a + b
}

//
class ScientificCalc(baseIn: Double) extends Calculator("CASIO") {
  val base = baseIn
  // Would be overridden in subclasses.
  def log(m: Int): Double = math.log(m) / math.log(base)  // How to default args?
}

// class MoreSciCalc extends ScientificCalc

// Abstract classes.
abstract class Geometry {
  def getArea(): Double  // Subclass to define this.
}

class Circle(r: Double) extends Geometry {
  def getArea(): Double = { r * r * 3.1415 }
}


// Traits.
trait Car {
  val brand: String
}

trait Sedan {
  val doorCount: Int
}

class BMW extends Car with Sedan {  // Notice 'with'.
  val brand = "BMW"
  val doorCount = 2
}  // Order of traits doesn't seem to matter as of now, check 4 commonn names.

// Similar to java interfaces (abstract base classes in python, they have only
// func signatures, not bodies.) traits seem to be. For interfaces, if a class
// extends an interface, and doesn't have all of its methods, that class must
// be declared as an abstract class.
//
//
// Though similar to abstract base classes, traits have some differences so use
// cases dictate what to use among trait or abstract class:
// Traits can't take params (for constructors). So if that's needed, the
//   abstract classes is the way to go.
// Traits allow multiple extensions (inheritance), only one class can be
//   extended.
//
// TODO: Types section is very unclear, need to learn that from somewhere else.
