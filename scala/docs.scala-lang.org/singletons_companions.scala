package companion
// Singletons are used for having static (independent of class instance)
// members. Like @classmethods or @staticmethods in python. When used with a
// companion class, it becomes a companion object and members behaves like
// @classmethod.


object SingletonObjectLogger {
  def info(message: String): Unit = println(s"INFO: $message")  // Unit => None
}

// This can now be imported in any package like:
// import companion.SingletonObjectLogger.info
// info("Log as info....")
// Only objects from static paths can be imported, not those defined inside
// other objects or classes.

// Companion objects and classes.
class Email(val username: String, val domainName: String)  // Just decleration.
// Notice 'val' in param declrn, optional, 'var' also works.

// This use of (companion) object can be seen in factories.
object Email {
  def fromString(emailString: String): Option[Email] = {
    emailString.split('@') match {
      case Array(a, b) => Some(new Email(a, b))
      case _ => None
    }
  }
}

// Due to yet unknown 'Some' & behaviour of 'Option' (0/1 Email container here)
// some of this code doesn't make sense to me yet but it has not been just
// copied, I probably typed it so many times in REPL that I now remember it
// well. Same with the above object definition.

var parsedEmail = Email.fromString("test@example.com")

// ?
parsedEmail match {
  case Some(email) => println(
    s"""Successfully parsed email address.
    | Username: ${email.username}
    | Domain name: ${email.domainName}
    """
    )
  case None => println("Couldn't parse any email in that string.")
}
