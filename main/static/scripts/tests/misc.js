module("Misc functions test", {});

test("capitalize test", function(assert){
    var asdf = "asdf";
    equals("Asdf", asdf.capitalize());

    var spacedOut = "spaced out";
    equals("Spaced out", spacedOut.capitalize());
});

test("getRandomInterval test", function(assert){
    for(var i = 0; i < 100; i++){
        ok(1 < Random.getRandomInterval(1, 100) < 100);
    }
});

test("getRandomInt test", function(assert){
    for(var i = 0; i < 100; i++){
        var r = Random.getRandomInt();
        ok(1 < r < 100);
        var ri = Math.floor(r);
        equals(r, ri);
    }
});

test("getRandomIntInclusiveTest", function(assert){
    for(var i = 0; i < 100; i++){
        var r = Random.getRandomIntInclusive();
        ok(1 <= r <= 100);
        var ri = Math.floor(r);
        equals(r, ri);
    }
});

test("random choice test", function(assert){
    var s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "1", "2", "3", "4"];
    for(var i = 0; i < 100; i++){
        var item = Random.choice(s);
        ok(s.indexOf(item) > -1);
    }
}):
