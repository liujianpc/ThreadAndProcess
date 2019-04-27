import multiprocessing
import time


def func(msg):
    for i in xrange(3):
        print msg, "at %s" % time.time()


if __name__ == "__main__":
    for i in xrange(10):
        msg = "hello %d" % i
        p = multiprocessing.Process(target=func, args=(msg,))
        p.start()

    print "Sub-process(es) done."
