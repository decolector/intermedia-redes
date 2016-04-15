import com.temboo.core.*;
import com.temboo.Library.Twitter.Search.*;

// Create a session using your Temboo account application details
TembooSession session = new TembooSession("account", "app name", "temboo key");

String[] tweet_texts;
PFont font;

void setup() {
  // Run the Tweets Choreo function
  size(800, 600);
  font = loadFont("Serif-24.vlw");
  textFont(font);
  tweet_texts = new String[0];
  runTweetsChoreo();
}

void runTweetsChoreo() {
  // Create the Choreo object using your Temboo session
  Tweets tweetsChoreo = new Tweets(session);

  // Set inputs
  tweetsChoreo.setQuery("justin bieber");
  tweetsChoreo.setAccessToken("access token");
  tweetsChoreo.setConsumerKey("consumer key");
  tweetsChoreo.setConsumerSecret("consumer secret");
  tweetsChoreo.setAccessTokenSecret("access token secret");
  tweetsChoreo.setCount("5");


  // Run the Choreo and store the results
  TweetsResultSet tweetsResults = tweetsChoreo.run();
  
  
  // Print results
  println(tweetsResults.getLimit());
  println(tweetsResults.getRemaining());
  println(tweetsResults.getReset());
  println(tweetsResults.getResponse());
  JSONObject response = parseJSONObject(tweetsResults.getResponse());
  parseTweets(response);

}

void parseTweets(JSONObject response){
  JSONArray statuses = response.getJSONArray("statuses");
  for(int i = 0; i < statuses.size(); i++){
   JSONObject tweet = statuses.getJSONObject(i);
   String text = tweet.getString("text");
   println(text);
   tweet_texts = (String[])append(tweet_texts, text);
  }
  
}

void draw(){
    background(0);
    fill(255);
    for(int i = 0; i < tweet_texts.length; i++){
      text(tweet_texts[i], 100, i* 50);
    }
}